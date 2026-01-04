function renderGames(games) {
  const area = document.getElementById("livearea");

  if (!area) {
    console.error("No existe #livearea");
    return;
  }

  area.innerHTML = "";

  games.forEach(game => {
    const app = document.createElement("div");
    app.className = "app";

    const img = document.createElement("img");
    img.src = game.cover;

    img.onerror = () => {
      img.remove();
      const fallback = document.createElement("div");
      fallback.className = "fallback";
      fallback.textContent = game.title;
      app.appendChild(fallback);
    };

    app.appendChild(img);

    app.onclick = () => {
      window.open(game.link, "_blank");
    };

    area.appendChild(app);
  });

  console.log("Render OK:", games.length);
}

// 🔴 ESTO ES CRÍTICO 🔴
window.addEventListener("DOMContentLoaded", () => {
  if (typeof GAMES !== "undefined") {
    renderGames(GAMES);
  } else {
    console.error("GAMES no definido");
  }
});
