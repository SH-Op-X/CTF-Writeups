package main

import (
	"game/game"
	"os/exec"
)

func main() {
	cmd := exec.Command("python3", "/bot.py")
	cmd.Start()

	game := game.NewGame()

	game.Run()
}
