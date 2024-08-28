package game

import (
	"errors"
	"fmt"
	"math/rand"
	"net"
	"os"
	"strconv"
	"strings"
	"time"
)

const PingTimeout = 8
const TimeToStart = 10

type Player struct {
	Id       int
	Name     string
	Position int
	Conn     net.Conn
	LastPing int64
}

type Game struct {
	Players  map[int]Player
	FullTime int64
	Started  bool
}

func NewGame() *Game {
	return &Game{Players: make(map[int]Player)}
}

func PayloadNewPlayer(name string, position int) string {
	return fmt.Sprintf("N|%s|%d;", name, position)
}

func PayloadMovePlayer(name string, position int) string {
	return fmt.Sprintf("M|%s|%d;", name, position)
}

func PayloadRemovePlayer(id int) string {
	return fmt.Sprintf("R|%d;", id)
}

func PayloadError(message string) string {
	return fmt.Sprintf("E|%s;", message)
}

func PayloadSuccess() string {
	return "S;"
}

func PayloadPong() string {
	return "Pong;"
}

func PayloadShoot(name string, position int, hit bool) string {
	return fmt.Sprintf("S|%s|%d|%t;", name, position, hit)
}

func PayloadGameFull() string {
	return "F;"
}

func PayloadGameStart() string {
	return "G;"
}

func PayloadJoin(id int) string {
	return fmt.Sprintf("J|%d;", id)
}

func GenerateId() int {
	return rand.Intn(100)
}

func (g *Game) AddPlayer(conn net.Conn, name string) error {
	name = strings.TrimSpace(name)

	if len(name) < 3 || len(name) > 10 {
		return errors.New("Invalid name")
	}

	for i := 0; i < len(name); i++ {
		if name[i] < 'a' || name[i] > 'z' {
			return errors.New("Invalid name")
		}
	}

	if len(g.Players) >= 2 {
		g.FullTime = time.Now().Unix()
		return errors.New("Game is full")
	}

	for _, player := range g.Players {
		if player.Name == name {
			return errors.New("Name already taken")
		}
	}

	playerId := GenerateId()
	for {
		if _, ok := g.Players[playerId]; ok {
			playerId = GenerateId()
		} else {
			break
		}
	}

	g.Players[playerId] = Player{Id: playerId, Name: name, Position: 0, Conn: conn, LastPing: time.Now().Unix()}

	g.Broadcast(PayloadNewPlayer(name, g.Players[playerId].Position))

	for _, player := range g.Players {
		if player.Conn != conn {
			player.Conn.Write([]byte(PayloadNewPlayer(player.Name, player.Position)))
		}
	}

	conn.Write([]byte(PayloadJoin(playerId)))

	if len(g.Players) == 2 {
		g.FullTime = time.Now().Unix()
		g.Broadcast(PayloadGameFull())

		for _, player := range g.Players {
			player.Position = 0
			g.Players[player.Id] = player
		}
	}

	return nil
}

func (g *Game) MovePlayer(id int, position int) error {
	player, ok := g.Players[id]

	if !ok {
		return errors.New("Player not found")
	}

	if position != 0 && position != 1 {
		return errors.New("Invalid move")
	}

	if position == 0 {
		position = -1
	}

	player.Position += position
	if player.Position < 0 {
		player.Position = 0
	}
	if player.Position >= 9 {
		player.Position = 8
	}
	g.Players[id] = player

	g.Broadcast(PayloadMovePlayer(player.Name, player.Position))

	return nil
}

func (g *Game) Shoot(id int) error {
	player, ok := g.Players[id]

	if !ok {
		return errors.New("Player not found")
	}

	if !g.Started {
		return errors.New("Game not started")
	}

	otherPlayer := Player{}
	found := false

	for _, p := range g.Players {
		if p.Id != id {
			otherPlayer = p
			found = true
			break
		}
	}

	if !found {
		return errors.New("Other player not found")
	}

	hit := player.Position == otherPlayer.Position && player.Position != 3

	g.Broadcast(PayloadShoot(player.Name, player.Position, hit))

	if hit {
		FLAG := os.Getenv("FLAG")
		if FLAG == "" {
			FLAG = "The flag should be here. If you see this on remote, contact an admin"
		}
		player.Conn.Write([]byte(PayloadError(FLAG)))
	}

	return nil
}

func (g *Game) RemovePlayer(id int) error {
	player, ok := g.Players[id]
	if !ok {
		return errors.New("Player not found")
	}

	player.Conn.Close()
	delete(g.Players, id)
	g.FullTime = 0
	g.Started = false

	g.Broadcast(PayloadRemovePlayer(id))

	return nil
}

func (g *Game) Broadcast(payload string) error {
	fmt.Println("Broadcasting", payload)
	for _, player := range g.Players {
		_, err := player.Conn.Write([]byte(payload))

		if err != nil {
			fmt.Println("Error broadcasting to", player.Conn.RemoteAddr().String(), err)
			g.RemovePlayer(player.Id)
			continue
		}
	}

	return nil
}

func (g *Game) Ping(id int) error {
	player, ok := g.Players[id]

	if !ok {
		return errors.New("Player not found")
	}

	player.LastPing = time.Now().Unix()
	g.Players[id] = player

	return nil
}

func (g *Game) Clean() {
	for id, player := range g.Players {
		if time.Now().Unix()-player.LastPing > PingTimeout {
			g.RemovePlayer(id)
		}
	}
}

func (g *Game) handleConnection(conn net.Conn) {
	defer conn.Close()

	fmt.Println("New connection from", conn.RemoteAddr().String())

	for {
		buffer := make([]byte, 0, 1024)
		conn.SetReadDeadline(time.Now().Add(time.Second * 30))
		tempBuffer := make([]byte, 1)
		n := 0
		for {
			tempN, err := conn.Read(tempBuffer)
			if tempN == 0 || err != nil {
				return
			}
			if tempBuffer[0] == ';' {
				break
			}
			buffer = append(buffer, tempBuffer[0])
			n += 1
		}

		fmt.Println("Received", string(buffer[:n]), "from", conn.RemoteAddr().String())

		playerExists := false
		for _, player := range g.Players {
			if player.Conn == conn {
				playerExists = true
				break
			}
		}

		switch string(buffer[0]) {
		case "N":
			err := g.AddPlayer(conn, string(buffer[2:n]))
			if err != nil {
				conn.Write([]byte(PayloadError(err.Error())))
				continue
			}
		}

		if !playerExists {
			continue
		}

		i := 0
		for i = 0; i < n; i++ {
			if buffer[i] == '|' {
				break
			}
		}

		if i == n {
			conn.Write([]byte(PayloadError("Invalid payload")))
			continue
		}

		playerId, err := strconv.Atoi(string(buffer[:i]))

		if err != nil {
			conn.Write([]byte(PayloadError("Invalid payload")))
			continue
		}

		if _, ok := g.Players[playerId]; !ok {
			conn.Write([]byte(PayloadError("Player not found")))
			continue
		}

		buffer = buffer[i+1 : n]

		switch string(buffer[0]) {
		case "M":
			position, err := strconv.Atoi(string(buffer[2]))
			if err != nil {
				conn.Write([]byte(PayloadError("Invalid payload")))
				continue
			}
			err = g.MovePlayer(playerId, position)
			if err != nil {
				conn.Write([]byte(PayloadError(err.Error())))
				continue
			}
		case "P":
			err := g.Ping(playerId)
			if err != nil {
				conn.Write([]byte(PayloadError(err.Error())))
				continue
			}
			conn.Write([]byte(PayloadPong()))
		case "S":
			err := g.Shoot(playerId)
			if err != nil {
				conn.Write([]byte(PayloadError(err.Error())))
				continue
			}
		}
	}
}

func (g *Game) Run() {
	fmt.Println("Starting game server")
	ln, err := net.Listen("tcp", ":1337")

	if err != nil {
		panic(err)
	}

	defer ln.Close()

	fmt.Println("Server started")

	go func() {
		for {
			if g.FullTime != 0 && time.Now().Unix()-g.FullTime > TimeToStart {
				g.FullTime = 0
				g.Started = true
				fmt.Println("Game started")
				g.Broadcast(PayloadGameStart())
			}
			time.Sleep(time.Second)
		}
	}()

	for {
		conn, err := ln.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			continue
		}

		go g.handleConnection(conn)

		if time.Now().Unix()-g.FullTime > PingTimeout {
			g.Clean()
		}

		if len(g.Players) < 2 {
			if g.FullTime != 0 {
				g.Broadcast(PayloadError("Player disconnected"))
			}
			g.FullTime = 0
		}
	}
}
