// disc/01/main.js
import httpsProxyAgent from "https-proxy-agent";
import env from "env";

// all_proxy=socks5://127.0.0.1:7890
function httpsAgent() {
	// @ts-ignore
	return new httpsProxyAgent( {
		host: '127.0.0.1',
		port: 7890,
		protocol: 'socks5'
	} );
}

async function test(messages) {
  const apiKey = env.getenv("OPENAI_API_KEY");
  const result = await fetch(`https://api.openai.com/v1/chat/completions`, {
    agent: httpsAgent(),
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
    method: "POST",
    body: JSON.stringify({
      messages,
      model: "gpt-3.5-turbo",
      temperature: 0.5,
      max_tokens: 4096,
      stream: true,
    })
  });
  return result
}

async function main() {
  const r = await test("What's your name?").catch(console.log);
  console.log("result：",r);
}

main();