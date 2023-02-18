const { spawn } = require("child_process");

const button = document.getElementById("getNumbers");
const resultDiv = document.getElementById("result");

button.addEventListener("click", async () => {
  const python = spawn("python", ["python/loop_dow.py"]);
  try {
    await python.stdout.on("data", (result) => {
      const { counter, counter2 } = JSON.parse(result);
      resultDiv.innerHTML = `The condition was satisfied <p class="text-bold text-md">${counter}</p> times. And from that, a total of <p class="text-bold text-md">${counter2}</p> days, Monday went below Friday's low.`;
    });
  } catch (err) {
    resultDiv.innerHTML += `${err.message}`;
  }
});
