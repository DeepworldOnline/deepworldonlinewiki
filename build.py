#!/usr/bin/env python3
"""Build the Deepworld Wiki index.html"""

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Deepworld Wiki</title>
<link rel="stylesheet" href="style.css">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' fill='%230e0a06'/><text x='4' y='24' font-size='22' fill='%23d4982c' font-family='monospace'>D</text></svg>">
</head>
<body>

<!-- ===== TOPBAR ===== -->
<div class="topbar">
  <div class="topbar-left">
    <button class="hamburger" onclick="toggleSidebar()" aria-label="Menu">&#9776;</button>
    <a href="#home" class="topbar-title">Deepworld Wiki</a>
  </div>
  <div class="search-box">
    <input type="text" id="searchInput" placeholder="Search wiki..." oninput="handleSearch()" onfocus="handleSearch()">
    <div class="search-results-dropdown" id="searchDropdown"></div>
  </div>
</div>

<!-- ===== SIDEBAR OVERLAY ===== -->
<div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>

<!-- ===== SIDEBAR ===== -->
<nav class="sidebar" id="sidebar">
  <div class="sidebar-logo">
    <svg viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect x="2" y="2" width="56" height="56" stroke="#d4982c" stroke-width="2" fill="#181008"/>
      <path d="M12 16h8v4h4v4h4v-4h4v-4h8v4h4v24h-4v4H16v-4h-4V16z" fill="#28b890" opacity="0.3"/>
      <path d="M18 20h4v4h-4z M26 20h4v4h-4z M34 20h4v4h-4z" fill="#d4982c"/>
      <path d="M14 28h32v2H14z" fill="#d4982c" opacity="0.6"/>
      <path d="M16 34h6v6h-6z M24 32h8v8h-8z M36 34h6v6h-6z" fill="#d4982c" opacity="0.4"/>
      <circle cx="30" cy="36" r="3" fill="#28b890"/>
      <path d="M20 46h20v2H20z" fill="#3a2008"/>
    </svg>
    <span>Deepworld</span>
  </div>

  <div class="nav-group">
    <div class="nav-group-title">Explore</div>
    <a href="#home" class="nav-link" data-page="home">Home</a>
    <a href="#guide" class="nav-link" data-page="guide">Guide</a>
    <a href="#community" class="nav-link" data-page="community">Community</a>
  </div>
  <div class="nav-group">
    <div class="nav-group-title">World</div>
    <a href="#biomes" class="nav-link" data-page="biomes">Biomes</a>
    <a href="#mobs" class="nav-link" data-page="mobs">Mobs & Creatures</a>
    <a href="#dungeons" class="nav-link" data-page="dungeons">Dungeons</a>
  </div>
  <div class="nav-group">
    <div class="nav-group-title">Equipment</div>
    <a href="#weapons" class="nav-link" data-page="weapons">Weapons</a>
    <a href="#tools" class="nav-link" data-page="tools">Tools</a>
    <a href="#accessories" class="nav-link" data-page="accessories">Accessories</a>
  </div>
  <div class="nav-group">
    <div class="nav-group-title">Crafting</div>
    <a href="#items" class="nav-link" data-page="items">Items & Resources</a>
    <a href="#machines" class="nav-link" data-page="machines">Machines</a>
    <a href="#skills" class="nav-link" data-page="skills">Skills</a>
  </div>
  <div class="nav-group">
    <div class="nav-group-title">Reference</div>
    <a href="#catalog" class="nav-link" data-page="catalog">Sprite Catalog</a>
  </div>

  <a href="https://discord.gg/deepworld" target="_blank" class="sidebar-discord">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.317 4.37a19.791 19.791 0 00-4.885-1.515.074.074 0 00-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 00-5.487 0 12.64 12.64 0 00-.617-1.25.077.077 0 00-.079-.037A19.736 19.736 0 003.677 4.37a.07.07 0 00-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 00.031.057 19.9 19.9 0 005.993 3.03.078.078 0 00.084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 00-.041-.106 13.107 13.107 0 01-1.872-.892.077.077 0 01-.008-.128 10.2 10.2 0 00.372-.292.074.074 0 01.077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 01.078.01c.12.098.246.198.373.292a.077.077 0 01-.006.127 12.299 12.299 0 01-1.873.892.077.077 0 00-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 00.084.028 19.839 19.839 0 006.002-3.03.077.077 0 00.032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 00-.031-.03z"/></svg>
    Discord
  </a>
</nav>

<!-- ===== MAIN CONTENT ===== -->
<main class="main">

<!-- ==================== HOME PAGE ==================== -->
<div class="page" id="page-home">
  <div class="welcome-banner">
    <div class="banner-header">
      <svg width="36" height="36" viewBox="0 0 60 60" fill="none"><rect x="2" y="2" width="56" height="56" stroke="#d4982c" stroke-width="2" fill="#181008"/><path d="M12 16h8v4h4v4h4v-4h4v-4h8v4h4v24h-4v4H16v-4h-4V16z" fill="#28b890" opacity="0.3"/><path d="M18 20h4v4h-4z M26 20h4v4h-4z M34 20h4v4h-4z" fill="#d4982c"/><circle cx="30" cy="36" r="3" fill="#28b890"/></svg>
      <h1>Welcome to the Deepworld Wiki</h1>
    </div>
    <div class="banner-body">
      <p><strong>Deepworld</strong> is a post-apocalyptic 2D sandbox crafting MMO originally developed by Bytebin (2012&ndash;2019). The game features steampunk-inspired weapons, mechanical creatures, seven unique biomes, and a deep crafting system. The community has revived the game through Brainwine private servers and a new community effort.</p>
      <p>This wiki contains comprehensive information about every biome, mob, weapon, tool, skill, and crafting recipe in the game.</p>
      <a href="https://discord.gg/deepworld" target="_blank" class="discord-btn">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.317 4.37a19.791 19.791 0 00-4.885-1.515.074.074 0 00-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 00-5.487 0 12.64 12.64 0 00-.617-1.25.077.077 0 00-.079-.037A19.736 19.736 0 003.677 4.37a.07.07 0 00-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 00.031.057 19.9 19.9 0 005.993 3.03.078.078 0 00.084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 00-.041-.106 13.107 13.107 0 01-1.872-.892.077.077 0 01-.008-.128 10.2 10.2 0 00.372-.292.074.074 0 01.077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 01.078.01c.12.098.246.198.373.292a.077.077 0 01-.006.127 12.299 12.299 0 01-1.873.892.077.077 0 00-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 00.084.028 19.839 19.839 0 006.002-3.03.077.077 0 00.032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 00-.031-.03z"/></svg>
        Join the Deepworld Discord
      </a>
    </div>
  </div>

  <h2>Explore the Wiki</h2>
  <div class="cat-grid">
    <a class="cat-card" href="#biomes">
      <svg viewBox="0 0 40 40" fill="none"><rect x="2" y="20" width="36" height="18" fill="#28b890" opacity="0.3" stroke="#28b890"/><circle cx="12" cy="14" r="6" fill="#28b890" opacity="0.5"/><circle cx="28" cy="10" r="8" fill="#28b890" opacity="0.4"/><rect x="8" y="16" width="2" height="8" fill="#3a2008"/><rect x="7" y="12" width="4" height="6" fill="#28b890" opacity="0.7"/></svg>
      <div class="cat-label">Biomes</div>
    </a>
    <a class="cat-card" href="#mobs">
      <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="16" r="10" fill="#cc3344" opacity="0.3" stroke="#cc3344"/><circle cx="16" cy="14" r="2" fill="#cc3344"/><circle cx="24" cy="14" r="2" fill="#cc3344"/><path d="M14 20 q6 4 12 0" stroke="#cc3344" stroke-width="1.5"/><path d="M10 26 l4 8 M30 26 l-4 8 M16 28 l0 8 M24 28 l0 8" stroke="#cc3344" stroke-width="1.5"/></svg>
      <div class="cat-label">Mobs</div>
    </a>
    <a class="cat-card" href="#weapons">
      <svg viewBox="0 0 40 40" fill="none"><rect x="18" y="4" width="4" height="24" fill="#d4982c" opacity="0.7"/><rect x="10" y="26" width="20" height="3" fill="#d4982c"/><rect x="16" y="29" width="8" height="6" fill="#3a2008"/><circle cx="20" cy="32" r="1" fill="#d4982c"/></svg>
      <div class="cat-label">Weapons</div>
    </a>
    <a class="cat-card" href="#tools">
      <svg viewBox="0 0 40 40" fill="none"><path d="M12 8 L20 28 L28 8" stroke="#d4982c" stroke-width="2" fill="none"/><rect x="14" y="28" width="12" height="4" fill="#d4982c" opacity="0.5"/><path d="M10 6 h20 v4 h-20z" fill="#88bbdd" opacity="0.5"/></svg>
      <div class="cat-label">Tools</div>
    </a>
    <a class="cat-card" href="#items">
      <svg viewBox="0 0 40 40" fill="none"><polygon points="20,4 36,16 30,36 10,36 4,16" fill="#aa55ff" opacity="0.3" stroke="#aa55ff"/><polygon points="20,10 30,18 26,32 14,32 10,18" fill="#aa55ff" opacity="0.2"/></svg>
      <div class="cat-label">Items</div>
    </a>
    <a class="cat-card" href="#skills">
      <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="14" stroke="#28b890" stroke-width="2" fill="none"/><path d="M20 8 v24 M8 20 h24" stroke="#28b890" stroke-width="1.5"/><circle cx="20" cy="20" r="4" fill="#28b890" opacity="0.5"/></svg>
      <div class="cat-label">Skills</div>
    </a>
    <a class="cat-card" href="#accessories">
      <svg viewBox="0 0 40 40" fill="none"><ellipse cx="20" cy="20" rx="14" ry="10" fill="#d4982c" opacity="0.2" stroke="#d4982c"/><circle cx="20" cy="14" r="5" fill="#d4982c" opacity="0.4"/><rect x="16" y="24" width="8" height="8" fill="#d4982c" opacity="0.3"/></svg>
      <div class="cat-label">Accessories</div>
    </a>
    <a class="cat-card" href="#machines">
      <svg viewBox="0 0 40 40" fill="none"><rect x="8" y="12" width="24" height="20" fill="#3a2008" stroke="#d4982c"/><circle cx="20" cy="22" r="6" stroke="#d4982c" stroke-width="2" fill="none"/><rect x="18" y="8" width="4" height="6" fill="#d4982c"/><circle cx="14" cy="18" r="1.5" fill="#28b890"/><circle cx="26" cy="18" r="1.5" fill="#cc3344"/></svg>
      <div class="cat-label">Machines</div>
    </a>
    <a class="cat-card" href="#dungeons">
      <svg viewBox="0 0 40 40" fill="none"><rect x="6" y="8" width="28" height="28" fill="#1c1208" stroke="#d4982c"/><rect x="14" y="28" width="12" height="8" fill="#3a2008"/><path d="M20 8 L6 20 M20 8 L34 20" stroke="#d4982c" stroke-width="1.5"/><rect x="16" y="14" width="3" height="4" fill="#d4982c" opacity="0.5"/><rect x="22" y="14" width="3" height="4" fill="#d4982c" opacity="0.5"/></svg>
      <div class="cat-label">Dungeons</div>
    </a>
    <a class="cat-card" href="#guide">
      <svg viewBox="0 0 40 40" fill="none"><rect x="8" y="6" width="24" height="30" fill="#1c1208" stroke="#d4982c"/><rect x="12" y="10" width="16" height="2" fill="#d4982c" opacity="0.6"/><rect x="12" y="16" width="16" height="1" fill="#d4982c" opacity="0.3"/><rect x="12" y="20" width="12" height="1" fill="#d4982c" opacity="0.3"/><rect x="12" y="24" width="14" height="1" fill="#d4982c" opacity="0.3"/><rect x="12" y="28" width="10" height="1" fill="#d4982c" opacity="0.3"/></svg>
      <div class="cat-label">Guide</div>
    </a>
    <a class="cat-card" href="#community">
      <svg viewBox="0 0 40 40" fill="none"><circle cx="14" cy="16" r="5" fill="#28b890" opacity="0.4"/><circle cx="26" cy="16" r="5" fill="#28b890" opacity="0.4"/><circle cx="20" cy="28" r="5" fill="#d4982c" opacity="0.4"/><path d="M14 21 L20 23 L26 21" stroke="#d4982c" stroke-width="1"/></svg>
      <div class="cat-label">Community</div>
    </a>
    <a class="cat-card" href="#catalog">
      <svg viewBox="0 0 40 40" fill="none"><rect x="4" y="4" width="14" height="14" fill="#d4982c" opacity="0.3" stroke="#d4982c"/><rect x="22" y="4" width="14" height="14" fill="#28b890" opacity="0.3" stroke="#28b890"/><rect x="4" y="22" width="14" height="14" fill="#aa55ff" opacity="0.3" stroke="#aa55ff"/><rect x="22" y="22" width="14" height="14" fill="#cc3344" opacity="0.3" stroke="#cc3344"/></svg>
      <div class="cat-label">Sprite Catalog</div>
    </a>
  </div>

  <div class="card">
    <div class="card-header">Revival Status</div>
    <div class="card-body">
      <p>The original Deepworld servers shut down in 2019. The community has kept the game alive through:</p>
      <ul style="margin-left:18px;margin-bottom:8px;">
        <li><strong>Brainwine</strong> &mdash; An open-source private server (<a href="https://github.com/kuroppoi/brainwine" target="_blank">github.com/kuroppoi/brainwine</a>)</li>
        <li><strong>Community Revival Server</strong> &mdash; A new server with a custom Windows client</li>
        <li><strong>Active Discord</strong> &mdash; Community coordination and updates</li>
      </ul>
    </div>
  </div>

  <div class="wiki-footer">
    Deepworld Wiki &mdash; Community-maintained. Not affiliated with Bytebin. Game data from config files and community research.
  </div>
</div>

<!-- ==================== BIOMES PAGE ==================== -->
<div class="page" id="page-biomes">
  <h1>Biomes</h1>
  <p>Deepworld features 7 distinct biomes, each with unique resources, enemies, environmental mechanics, and terrain. Worlds generate with a specific biome type that determines what you'll find.</p>

  <!-- TEMPERATE -->
  <div class="biome-section clearfix" id="biome-temperate">
    <div class="infobox">
      <div class="infobox-header">Temperate</div>
      <img class="infobox-img" src="https://static.wikia.nocookie.net/deepworld/images/6/6f/Screenshot_2025-10-28_220759.png" alt="Temperate Biome" onerror="this.style.display='none'">
      <div class="infobox-row"><div class="infobox-label">Type</div><div class="infobox-value">Starter Biome</div></div>
      <div class="infobox-row"><div class="infobox-label">Mechanic</div><div class="infobox-value">Acid Rain</div></div>
      <div class="infobox-row"><div class="infobox-label">Resources</div><div class="infobox-value">Green Crystals, Copper, Iron, Wood</div></div>
      <div class="infobox-row"><div class="infobox-label">Exclusive</div><div class="infobox-value">Green Crystals</div></div>
      <div class="infobox-row"><div class="infobox-label">Enemies</div><div class="infobox-value">Brains, Automata, Terrapus, Acid Terrapus</div></div>
      <div class="infobox-row"><div class="infobox-label">Absent</div><div class="infobox-value">Diamonds, Platinum, Bloodstone, Beryllium, Marble</div></div>
    </div>
    <h2>Temperate</h2>
    <p>The default starter biome with grassy terrain, trees, and varied underground ores. New worlds start with acid rain at 100% acidity. As you find all 8 Purifier parts and assemble the Purifier, acid rain converts to normal rain, and the biome becomes lush enough for flowers and bulbs to grow.</p>
    <h4>Mushrooms (8 types)</h4>
    <p>Portabella, Oyster, Porcini, Willow, Amanita, Chanterelle, Morel, Acid Mushroom</p>
    <h4>Environment</h4>
    <p>Acid rain damages players without Exo-skin protection. The Purifier machine (8 parts found in green crates) neutralizes the acid rain when assembled. After purification, flowers and plants begin to grow naturally.</p>
  </div>

  <!-- DESERT -->
  <div class="biome-section clearfix" id="biome-desert">
    <div class="infobox">
      <div class="infobox-header">Desert</div>
      <img class="infobox-img" src="https://static.wikia.nocookie.net/deepworld/images/1/14/Screenshot_2025-10-29_124204.png" alt="Desert Biome" onerror="this.style.display='none'">
      <div class="infobox-row"><div class="infobox-label">Type</div><div class="infobox-value">Arid Biome</div></div>
      <div class="infobox-row"><div class="infobox-label">Mechanic</div><div class="infobox-value">Dehydration</div></div>
      <div class="infobox-row"><div class="infobox-label">Resources</div><div class="infobox-value">Beryllium, Yellow Crystals, Sandstone</div></div>
      <div class="infobox-row"><div class="infobox-label">Exclusive</div><div class="infobox-value">Beryllium</div></div>
      <div class="infobox-row"><div class="infobox-label">Enemies</div><div class="infobox-value">Scorpions, Sand Worms, Armadillos</div></div>
      <div class="infobox-row"><div class="infobox-label">Fossils</div><div class="infobox-value">Raptor, Pterodactyl</div></div>
    </div>
    <h2>Desert</h2>
    <p>A barren biome where cacti replace trees and sandstone ruins dot the landscape. The desert has a dehydration mechanic &mdash; a Hydration bar that depletes over time. Players must carry and use Jars of Water to stay hydrated.</p>
    <h4>Exclusive Resource: Beryllium</h4>
    <p>Beryllium ore is found only in Desert biomes and is required for crafting Energy weapons, weapon upgrade kits, and other advanced items.</p>
    <h4>Mushrooms</h4>
    <p>Portabella, Oyster, Porcini, Chanterelle, Morel, Acid, Anbaric Mushroom</p>
    <h4>Unique Creatures</h4>
    <p>The desert is home to Scorpions, Large Scorpions, Sand Worms, and the friendly Armadillo.</p>
  </div>

  <!-- ARCTIC -->
  <div class="biome-section clearfix" id="biome-arctic">
    <div class="infobox">
      <div class="infobox-header">Arctic</div>
      <img class="infobox-img" src="https://static.wikia.nocookie.net/deepworld/images/8/82/Screenshot_2025-10-29_004813.png" alt="Arctic Biome" onerror="this.style.display='none'">
      <div class="infobox-row"><div class="infobox-label">Type</div><div class="infobox-value">Frozen Biome</div></div>
      <div class="infobox-row"><div class="infobox-label">Mechanic</div><div class="infobox-value">Cold / Warmth Drain</div></div>
      <div class="infobox-row"><div class="infobox-label">Resources</div><div class="infobox-value">Diamonds, Blue Crystals, Onyx (100%)</div></div>
      <div class="infobox-row"><div class="infobox-label">Exclusive</div><div class="infobox-value">Diamonds</div></div>
      <div class="infobox-row"><div class="infobox-label">Enemies</div><div class="infobox-value">Brains, Automata, Frost Terrapus</div></div>
      <div class="infobox-row"><div class="infobox-label">Bunkers</div><div class="infobox-value">Ice Sculpture, Present</div></div>
    </div>
    <h2>Arctic</h2>
    <p>A barren frozen biome with no trees and scattered ruins. The cold mechanic drains the player's warmth &mdash; without an Exo-skin, players lose HP over time. Arctic biomes are the only source of Diamond ore and have a 100% Onyx spawn rate.</p>
    <h4>Exclusive Resources</h4>
    <p>Diamonds are found only in Arctic biomes and are essential for Diamond-tier tools, weapons, and the Diamond Weapon Kit.</p>
    <h4>Special Bunkers</h4>
    <p>The Arctic has unique bunker types: Ice Sculpture Bunkers containing ice sculptures, and Present/Candy Cane Bunkers with candy canes, presents, and unique seasonal loot.</p>
    <h4>Mushrooms</h4>
    <p>Portabella, Oyster, Porcini, Chanterelle, Arctic Mushroom</p>
  </div>

  <!-- HELL -->
  <div class="biome-section clearfix" id="biome-hell">
    <div class="infobox">
      <div class="infobox-header">Hell</div>
      <div class="infobox-row"><div class="infobox-label">Type</div><div class="infobox-value">Fire Biome</div></div>
      <div class="infobox-row"><div class="infobox-label">Mechanic</div><div class="infobox-value">Fire/Magma hazards</div></div>
      <div class="infobox-row"><div class="infobox-label">Resources</div><div class="infobox-value">Bloodstone</div></div>
      <div class="infobox-row"><div class="infobox-label">Machine</div><div class="infobox-value">Expiator</div></div>
      <div class="infobox-row"><div class="infobox-label">Enemies</div><div class="infobox-value">Skeleton Terrapus, Ghosts</div></div>
    </div>
    <h2>Hell</h2>
    <p>A fire-themed biome filled with magma and hazards. The Expiator machine is unique to this biome &mdash; it consists of 8 parts that must be found and assembled, similar to the Purifier. Skeleton Terrapus are the primary enemy here, immune to most weapon types. The biome contains Bloodstone as a resource.</p>
    <h4>Expiator Machine</h4>
    <p>The Expiator is a Hell-exclusive machine assembled from 8 parts. When completed, it releases ghosts and affects the biome's supernatural activity.</p>
  </div>

  <!-- DEEP -->
  <div class="biome-section clearfix" id="biome-deep">
    <div class="infobox">
      <div class="infobox-header">Deep</div>
      <div class="infobox-row"><div class="infobox-label">Type</div><div class="infobox-value">Underground</div></div>
      <div class="infobox-row"><div class="infobox-label">Mechanic</div><div class="infobox-value">Darkness</div></div>
      <div class="infobox-row"><div class="infobox-label">Notes</div><div class="infobox-value">Underground deep world</div></div>
    </div>
    <h2>Deep</h2>
    <p>An underground biome shrouded in darkness. Flashlights and light sources are essential for navigation. The Deep biome features unique underground terrain and resource deposits.</p>
  </div>

  <!-- BRAIN -->
  <div class="biome-section clearfix" id="biome-brain">
    <div class="infobox">
      <div class="infobox-header">Brain</div>
      <div class="infobox-row"><div class="infobox-label">Type</div><div class="infobox-value">Alien Biome</div></div>
      <div class="infobox-row"><div class="infobox-label">Enemies</div><div class="infobox-value">Baby Brains, all Brain types</div></div>
      <div class="infobox-row"><div class="infobox-label">Notes</div><div class="infobox-value">Baby Brain homeland</div></div>
    </div>
    <h2>Brain</h2>
    <p>The homeland of the Brain creatures. This biome is populated primarily by Baby Brains and other Brain variants. It serves as the origin point for Deepworld's most iconic enemy faction.</p>
  </div>

  <!-- SPACE -->
  <div class="biome-section clearfix" id="biome-space">
    <div class="infobox">
      <div class="infobox-header">Space</div>
      <div class="infobox-row"><div class="infobox-label">Type</div><div class="infobox-value">Space Biome</div></div>
      <div class="infobox-row"><div class="infobox-label">Exclusive</div><div class="infobox-value">Platinum</div></div>
      <div class="infobox-row"><div class="infobox-label">Added</div><div class="infobox-value">Christmas Update</div></div>
    </div>
    <h2>Space</h2>
    <p>The Space biome was released as a major Christmas update content addition. It is the exclusive source of Platinum ore, which is used to craft the highest tier of tools: Platinum Pickaxe, Platinum Shovel, Platinum Spade, and Platinum Net.</p>
  </div>
</div>

<!-- ==================== MOBS PAGE ==================== -->
<div class="page" id="page-mobs">
  <h1>Mobs & Creatures</h1>
  <p>Deepworld is populated with a variety of hostile, neutral, and friendly creatures. Each mob has specific stats, behaviors, and loot tables.</p>

  <!-- TERRAPUS FAMILY -->
  <div class="mob-family">
    <h2>Terrapus Family</h2>
    <p>The Terrapus (plural: Terrapi) are the most common aggressive mob in Deepworld. The name comes from "terra" (earth) + "octopus" &mdash; earth octopus. They do not follow players but can climb walls. Each variant is adapted to a specific biome element.</p>
    <table class="wiki-table">
      <thead>
        <tr><th>Name</th><th>HP</th><th>Damage</th><th>XP</th><th>Weakness</th><th>Defense</th><th>Biome</th></tr>
      </thead>
      <tbody>
        <tr><td>Juvenile Terrapus</td><td>0.5</td><td><span class="dmg dmg-piercing">Piercing 0.3</span></td><td>1</td><td>&mdash;</td><td>&mdash;</td><td>All (surface)</td></tr>
        <tr><td>Adult Terrapus</td><td>0.8</td><td><span class="dmg dmg-piercing">Piercing 0.5</span></td><td>2</td><td>Fire 0.3, Piercing 0.2, Crushing 0.3</td><td>Acid 0.2</td><td>All</td></tr>
        <tr><td>Fire Terrapus</td><td>1.5</td><td><span class="dmg dmg-fire">Fire 0.75</span></td><td>3</td><td>Cold 0.4, Crushing 0.2</td><td>Fire 1.3, Steam 1.1</td><td>Any (fire weapon spawn)</td></tr>
        <tr><td>Acid Terrapus</td><td>1.5</td><td><span class="dmg dmg-acid">Acid 0.55</span></td><td>3</td><td>Crushing 0.2</td><td>Acid 1.3</td><td>Temperate (rare)</td></tr>
        <tr><td>Skeleton Terrapus</td><td>2.0</td><td><span class="dmg dmg-energy">Energy 0.3</span></td><td>3</td><td>Crushing 0.2</td><td>Energy 1.3, Cold 0.5, Fire 0.5</td><td>Hell only</td></tr>
        <tr><td>Frost Terrapus</td><td>1.5</td><td><span class="dmg dmg-cold">Cold 0.55</span></td><td>3</td><td>Fire 0.4, Crushing 0.2</td><td>Cold 1.3</td><td>Arctic</td></tr>
        <tr><td>Queen Terrapus</td><td>25.0</td><td><span class="dmg dmg-piercing">Piercing 2.0</span></td><td>25</td><td>&mdash;</td><td>Acid 1.0, Cold 0.5, Energy 0.2, Crushing 0.6</td><td>Boss</td></tr>
        <tr><td>Pet Terrapus</td><td>&mdash;</td><td>None (friendly)</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>Red chest loot</td></tr>
      </tbody>
    </table>
  </div>

  <!-- BRAINS -->
  <div class="mob-family">
    <h2>Brains</h2>
    <p>Brains are among the most iconic enemies in Deepworld. Found in dungeons, Brain biomes, and mechanical maws, they attack with energy cannons and use force shields for defense. They are a primary source of Shillings.</p>
    <table class="wiki-table">
      <thead>
        <tr><th>Name</th><th>HP</th><th>Damage</th><th>XP</th><th>Notes</th></tr>
      </thead>
      <tbody>
        <tr><td>Tiny Brain</td><td>3</td><td><span class="dmg dmg-energy">Energy 0.3</span></td><td>5</td><td>Has force shield</td></tr>
        <tr><td>Juvenile Brain</td><td>7</td><td><span class="dmg dmg-energy">Energy 0.3</span></td><td>10</td><td>Has force shield, drops Shillings</td></tr>
        <tr><td>Adult Brain</td><td>11</td><td><span class="dmg dmg-energy">Energy 0.4</span></td><td>20</td><td>Drops Shillings (20), canisters</td></tr>
        <tr><td>Dire Adult Brain</td><td>18</td><td><span class="dmg dmg-energy">Energy 0.5</span></td><td>30</td><td>Drops Shillings (30), spawns from Pandora</td></tr>
        <tr><td>Brain Lord</td><td>34</td><td><span class="dmg dmg-energy">Energy 0.5</span></td><td>100</td><td>Boss. Drops Shillings (100), cloaks</td></tr>
      </tbody>
    </table>
  </div>

  <!-- AUTOMATA -->
  <div class="mob-family">
    <h2>Automata</h2>
    <p>Mechanical enemies found primarily in dungeons and scattered throughout the world. Weak to bludgeoning weapons (Sledgehammers, Tesla Club). Come in Walker and Flyer variants for each size.</p>
    <table class="wiki-table">
      <thead>
        <tr><th>Name</th><th>HP</th><th>XP</th><th>Loot</th><th>Variants</th></tr>
      </thead>
      <tbody>
        <tr><td>Small Automata</td><td>1.5</td><td>5</td><td>Iron rubble, brass rubble, canisters</td><td>Walker, Flyer</td></tr>
        <tr><td>Medium Automata</td><td>6</td><td>10</td><td>Iron/brass rubble, canisters</td><td>Walker, Flyer</td></tr>
        <tr><td>Large Automata</td><td>15</td><td>20</td><td>Canisters, ectoplasm</td><td>Walker, Flyer</td></tr>
      </tbody>
    </table>
    <p>Gun-equipped Automata variants also exist: Acid, Bullet, Energy, Flame, Frost, and Steam gun types.</p>
  </div>

  <!-- SUPERNATURAL -->
  <div class="mob-family">
    <h2>Supernatural</h2>
    <p>Ghostly and undead entities found in certain biomes and dungeons.</p>
    <table class="wiki-table">
      <thead>
        <tr><th>Name</th><th>HP</th><th>Damage</th><th>XP</th><th>Speed</th></tr>
      </thead>
      <tbody>
        <tr><td>Ghost</td><td>3</td><td>&mdash;</td><td>&mdash;</td><td>3</td></tr>
        <tr><td>Revenant</td><td>6</td><td><span class="dmg dmg-shadow">Shadow</span></td><td>10</td><td>3</td></tr>
        <tr><td>Dire Revenant</td><td>12</td><td><span class="dmg dmg-shadow">Shadow (burst 8)</span></td><td>20</td><td>5</td></tr>
        <tr><td>Revenant Lord</td><td>31</td><td><span class="dmg dmg-shadow">Shadow</span></td><td>80</td><td>4</td></tr>
      </tbody>
    </table>
  </div>

  <!-- DESERT CREATURES -->
  <div class="mob-family">
    <h2>Desert Creatures</h2>
    <p>Creatures unique to the Desert biome.</p>
    <table class="wiki-table">
      <thead>
        <tr><th>Name</th><th>HP</th><th>Damage</th><th>XP</th><th>Notes</th></tr>
      </thead>
      <tbody>
        <tr><td>Scorpion</td><td>1.75</td><td>&mdash;</td><td>3</td><td>Common desert enemy</td></tr>
        <tr><td>Large Scorpion</td><td>5.5</td><td><span class="dmg dmg-piercing">Piercing 0.9</span></td><td>5</td><td>Stronger variant</td></tr>
        <tr><td>Sand Worm</td><td>&mdash;</td><td><span class="dmg dmg-fire">Fire 1.0</span></td><td>&mdash;</td><td>Emerges from sand</td></tr>
        <tr><td>Armadillo</td><td>2.0</td><td>None</td><td>&mdash;</td><td>Friendly, passive creature</td></tr>
      </tbody>
    </table>
  </div>

  <!-- OTHER CREATURES -->
  <div class="mob-family">
    <h2>Other Creatures</h2>
    <h4>Small Animals</h4>
    <table class="wiki-table">
      <thead>
        <tr><th>Name</th><th>HP</th><th>Behavior</th><th>Notes</th></tr>
      </thead>
      <tbody>
        <tr><td>Rat</td><td>0.9</td><td>Friendly</td><td>Found underground</td></tr>
        <tr><td>Bat</td><td>1.1</td><td>Neutral</td><td>Found in caves</td></tr>
        <tr><td>Roach</td><td>&mdash;</td><td>Neutral</td><td>Small pest</td></tr>
        <tr><td>Large Roach</td><td>&mdash;</td><td>Neutral</td><td>Larger variant</td></tr>
        <tr><td>Bunny</td><td>&mdash;</td><td>Friendly</td><td>Arctic variant exists</td></tr>
        <tr><td>Skunk</td><td>&mdash;</td><td>Friendly</td><td>Passive</td></tr>
      </tbody>
    </table>

    <h4>Birds (all friendly)</h4>
    <p>Crow, Vulture, Bluejay, Cardinal, Seagull &mdash; all are friendly and non-hostile.</p>

    <h4>Butterflies (8 types, catchable with Net)</h4>
    <p>Eight varieties of butterflies can be found and caught using a Net tool. Higher-tier nets increase catch chance.</p>

    <h4>Fish (8 types)</h4>
    <p>Almaco Jack, Angelfish, Clownfish, Codfish, Flame Hawkfish, Herring, Piranha, Sergeant Major</p>

    <h4>Anemones</h4>
    <p>Standard, Electric, Magenta, Red &mdash; found underwater.</p>
  </div>

  <!-- ANDROIDS -->
  <div class="mob-family">
    <h2>Androids</h2>
    <p>Androids are the rarest mobs in Deepworld &mdash; only 6 spawn per world. They are metallic-gold humanoid figures that wear hats.</p>
    <div class="card">
      <div class="card-header">Android Mechanics</div>
      <div class="card-body">
        <ul style="margin-left:18px;">
          <li><strong>Free Loot:</strong> Each android gives free loot once per day per player</li>
          <li><strong>Consecutive Bonus:</strong> Collecting from the same android for 5 consecutive days grants a special item on the 5th day</li>
          <li><strong>Shilling Trade:</strong> Use Shillings to trade with androids (requires Barter skill)</li>
          <li><strong>Figurines:</strong> Use Shillings + marble/bloodstone ores to enlarge android figurines</li>
        </ul>
      </div>
    </div>
    <h4>Barter Androids</h4>
    <p>Special android NPCs designed for trading. Players with the Barter skill can exchange Shillings for items.</p>
  </div>

  <!-- PETS -->
  <div class="mob-family">
    <h2>Pets</h2>
    <p>Friendly companion creatures that follow the player.</p>
    <table class="wiki-table">
      <thead>
        <tr><th>Pet</th><th>Source</th></tr>
      </thead>
      <tbody>
        <tr><td>Pet Terrapus</td><td>Rare red chest loot</td></tr>
        <tr><td>Pet Crow</td><td>Special loot</td></tr>
        <tr><td>Pet Bunny</td><td>Special loot</td></tr>
        <tr><td>Pet Skunk</td><td>Special loot</td></tr>
        <tr><td>Pet Vulture</td><td>Special loot</td></tr>
        <tr><td>Automata Cat</td><td>Crafted</td></tr>
        <tr><td>Automata Dog</td><td>Crafted</td></tr>
        <tr><td>Automata Pet</td><td>Crafted</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ==================== WEAPONS PAGE ==================== -->
<div class="page" id="page-weapons">
  <h1>Weapons & Combat</h1>
  <p>Deepworld features ranged firearms, melee weapons, and bombs. Ranged weapons consume steam to fire. Weapons can be upgraded using Diamond and Onyx Weapon Kits.</p>

  <h2>Gun Parts (Craft First)</h2>
  <p>Before crafting any ranged weapon, you need to craft the component parts:</p>
  <table class="wiki-table">
    <thead><tr><th>Part</th><th>Recipe</th></tr></thead>
    <tbody>
      <tr><td>Gun Barrel</td><td><span class="recipe"><span class="mat">1x Iron</span> <span class="plus">+</span> <span class="mat">1x Brass</span></span></td></tr>
      <tr><td>Pistol Stock</td><td><span class="recipe"><span class="mat">1x Iron</span> <span class="plus">+</span> <span class="mat">1x Wood</span></span></td></tr>
      <tr><td>Musket Stock</td><td><span class="recipe"><span class="mat">1x Iron</span> <span class="plus">+</span> <span class="mat">2x Wood</span></span></td></tr>
    </tbody>
  </table>

  <h2>Weapon Upgrade Kits</h2>
  <table class="wiki-table">
    <thead><tr><th>Kit</th><th>Upgrade</th><th>Recipe</th><th>Skill Req</th></tr></thead>
    <tbody>
      <tr><td class="rarity-rare">Diamond Weapon Kit</td><td>Base &rarr; MK2</td><td><span class="recipe"><span class="mat">3x Diamond</span> <span class="plus">+</span> <span class="mat">3x Iron</span> <span class="plus">+</span> <span class="mat">3x Beryllium</span> <span class="plus">+</span> <span class="mat">Schematic</span></span></td><td>Engineering 8</td></tr>
      <tr><td class="rarity-epic">Onyx Weapon Kit</td><td>Base &rarr; MK3</td><td><span class="recipe"><span class="mat">2x Onyx</span> <span class="plus">+</span> <span class="mat">3x Iron</span> <span class="plus">+</span> <span class="mat">3x Beryllium</span> <span class="plus">+</span> <span class="mat">Schematic</span></span></td><td>Engineering 10</td></tr>
      <tr><td class="rarity-rare">Diamond Turret Kit</td><td>Turret MK1 &rarr; MK2</td><td>&mdash;</td><td>&mdash;</td></tr>
      <tr><td class="rarity-epic">Onyx Turret Kit</td><td>Turret MK2 &rarr; MK3</td><td>&mdash;</td><td>&mdash;</td></tr>
    </tbody>
  </table>

  <h2>Ranged Weapons</h2>

  <h3>Non-Elemental</h3>
  <table class="wiki-table">
    <thead><tr><th>Weapon</th><th>Damage</th><th>Rate</th><th>Crafting</th><th>Skill</th></tr></thead>
    <tbody>
      <tr><td>Pistol</td><td><span class="dmg dmg-piercing">Piercing 0.175</span></td><td>2</td><td>Pistol Stock + Gun Barrel</td><td>Building 2</td></tr>
      <tr><td>Pistol MK2</td><td><span class="dmg dmg-piercing">Piercing 0.219</span></td><td>3</td><td>Diamond Weapon Kit</td><td>&mdash;</td></tr>
      <tr><td>Pistol MK3</td><td><span class="dmg dmg-piercing">Piercing 0.263</span></td><td>4</td><td>Onyx Weapon Kit</td><td>&mdash;</td></tr>
      <tr><td>Musket</td><td><span class="dmg dmg-piercing">Piercing 0.2</span></td><td>3</td><td>Musket Stock + 2x Gun Barrel</td><td>Building 3</td></tr>
      <tr><td>Musket MK2</td><td><span class="dmg dmg-piercing">Piercing 0.25</span></td><td>4</td><td>Diamond Weapon Kit</td><td>&mdash;</td></tr>
      <tr><td>Musket MK3</td><td><span class="dmg dmg-piercing">Piercing 0.3</span></td><td>5</td><td>Onyx Weapon Kit</td><td>&mdash;</td></tr>
    </tbody>
  </table>

  <h3>Steam Element</h3>
  <table class="wiki-table">
    <thead><tr><th>Weapon</th><th>Damage</th><th>Crafting</th><th>Skill</th></tr></thead>
    <tbody>
      <tr><td>Steam Pistol</td><td><span class="dmg dmg-steam">Fire 0.15</span></td><td>Pistol Stock + 2x Gun Barrel + 2x Brass + Iron + Blue Crystal</td><td>Engineering 3</td></tr>
      <tr><td>Steam Cannon</td><td><span class="dmg dmg-steam">Fire 0.225</span></td><td>Pistol Stock + 2x Gun Barrel + 6x Brass + 2x Iron + 2x Blue Crystal</td><td>Engineering 5</td></tr>
    </tbody>
  </table>

  <h3>Flame Element</h3>
  <table class="wiki-table">
    <thead><tr><th>Weapon</th><th>Damage</th><th>Crafting</th><th>Skill</th></tr></thead>
    <tbody>
      <tr><td>Flame Pistol</td><td><span class="dmg dmg-fire">Fire 0.25</span></td><td>Pistol Stock + 2x Gun Barrel + Brass + 2x Iron + Red Crystal</td><td>Engineering 5</td></tr>
      <tr><td>Flamethrower</td><td><span class="dmg dmg-fire">Fire 0.375</span></td><td>Pistol Stock + 2x Gun Barrel + 4x Brass + 2x Iron + 3x Red Crystal</td><td>Engineering 7</td></tr>
    </tbody>
  </table>

  <h3>Frost Element</h3>
  <table class="wiki-table">
    <thead><tr><th>Weapon</th><th>Damage</th><th>Crafting</th><th>Skill</th></tr></thead>
    <tbody>
      <tr><td>Frost Pistol</td><td><span class="dmg dmg-cold">Cold 0.25</span></td><td>Pistol Stock + 2x Gun Barrel + Brass + 2x Iron + Red Crystal</td><td>Engineering 5</td></tr>
      <tr><td>Frost Cannon</td><td><span class="dmg dmg-cold">Cold 0.375</span></td><td>Pistol Stock + 2x Gun Barrel + Brass + 2x Iron + 3x Red Crystal</td><td>Engineering 7</td></tr>
    </tbody>
  </table>

  <h3>Acid Element</h3>
  <table class="wiki-table">
    <thead><tr><th>Weapon</th><th>Damage</th><th>Crafting</th><th>Skill</th></tr></thead>
    <tbody>
      <tr><td>Acid Cannon</td><td><span class="dmg dmg-acid">Acid 0.3 (burst 3)</span></td><td>Pistol Stock + 2x Gun Barrel + 4x Brass + 5x Jar of Acid + 2x Red Crystal</td><td>Engineering 6</td></tr>
    </tbody>
  </table>

  <h3>Energy Element</h3>
  <table class="wiki-table">
    <thead><tr><th>Weapon</th><th>Damage</th><th>Crafting</th><th>Skill</th></tr></thead>
    <tbody>
      <tr><td>Energy Pistol</td><td><span class="dmg dmg-energy">Energy 0.225</span></td><td>Pistol Stock + 2x Gun Barrel + Brass + 2x Beryllium Ore + Red Crystal</td><td>Engineering 6</td></tr>
      <tr><td>Energy Cannon</td><td><span class="dmg dmg-energy">Energy 0.3375</span></td><td>Pistol Stock + 2x Gun Barrel + Brass + 4x Beryllium Ore + 3x Red Crystal + Schematic</td><td>Engineering 8</td></tr>
    </tbody>
  </table>

  <h2>Melee Weapons</h2>

  <h3>Slashing (Effective vs Organic Mobs)</h3>
  <table class="wiki-table">
    <thead><tr><th>Weapon</th><th>Damage</th><th>Crafting</th><th>Skill</th></tr></thead>
    <tbody>
      <tr><td>Hatchet</td><td><span class="dmg dmg-slash">Slashing 0.15</span></td><td>Wood + 2x Iron</td><td>Building 2</td></tr>
      <tr><td>Diamond Hatchet</td><td><span class="dmg dmg-slash">Slashing 0.2</span></td><td>3x Diamond Ore + 2x Brass + 2x Iron</td><td>Building 4</td></tr>
      <tr><td>Rapier</td><td><span class="dmg dmg-slash">Slashing 0.25</span></td><td>8x Iron + 2x Wood</td><td>Building 4</td></tr>
      <tr><td>Diamond Rapier</td><td><span class="dmg dmg-slash">Slashing 0.3</span></td><td>4x Diamond Ore + 5x Iron + 3x Brass</td><td>Building 6</td></tr>
      <tr><td>Onyx Rapier</td><td><span class="dmg dmg-slash">Slashing 0.35</span></td><td>3x Onyx + 5x Iron + 3x Brass</td><td>Building 8</td></tr>
    </tbody>
  </table>

  <h3>Bludgeoning (Effective vs Mechanical Mobs)</h3>
  <table class="wiki-table">
    <thead><tr><th>Weapon</th><th>Damage</th><th>Crit</th><th>Crafting</th><th>Skill</th></tr></thead>
    <tbody>
      <tr><td>Sledgehammer</td><td><span class="dmg dmg-crush">Bludgeoning 0.2</span></td><td>1%</td><td>Wood + 2x Iron Rubble</td><td>&mdash;</td></tr>
      <tr><td>Fine Sledgehammer</td><td><span class="dmg dmg-crush">Bludgeoning 0.25</span></td><td>2%</td><td>Wood + 2x Iron + Resin</td><td>Building 2</td></tr>
      <tr><td>Diamond Sledgehammer</td><td><span class="dmg dmg-crush">Bludgeoning 0.3</span></td><td>3%</td><td>4x Diamond Ore + 2x Iron + 2x Resin</td><td>Building 4</td></tr>
      <tr><td>Onyx Sledgehammer</td><td><span class="dmg dmg-crush">Bludgeoning 0.35</span></td><td>4%</td><td>3x Onyx + 2x Iron + 2x Resin</td><td>Building 6</td></tr>
      <tr><td>Tesla Club</td><td><span class="dmg dmg-energy">Energy 0.375</span></td><td>2.5%</td><td>2x Brass + 2x Iron + 5x Quartz Ore + Red Crystal + Schematic</td><td>Engineering 5</td></tr>
    </tbody>
  </table>

  <h3>Canes</h3>
  <table class="wiki-table">
    <thead><tr><th>Weapon</th><th>Damage</th><th>Crafting</th><th>Skill</th></tr></thead>
    <tbody>
      <tr><td>Cane</td><td><span class="dmg dmg-crush">Bludgeoning 0.075</span></td><td>5x Wood + Brass</td><td>Building 2</td></tr>
    </tbody>
  </table>

  <h2>Bombs</h2>
  <p>Bombs are throwable explosives with various effects. Some destroy the environment; others deal only mob damage.</p>
  <div class="bomb-grid">
    <div class="bomb-item"><div class="bomb-name">Bomb</div><div class="bomb-desc">Standard explosive, destroys blocks</div></div>
    <div class="bomb-item"><div class="bomb-name">Big Bomb</div><div class="bomb-desc">Larger blast radius</div></div>
    <div class="bomb-item"><div class="bomb-name">Mega Bomb</div><div class="bomb-desc">Massive blast radius</div></div>
    <div class="bomb-item"><div class="bomb-name">Mine</div><div class="bomb-desc">Proximity-triggered explosive</div></div>
    <div class="bomb-item"><div class="bomb-name">Fire Bomb</div><div class="bomb-desc">Fire damage, no block destruction</div></div>
    <div class="bomb-item"><div class="bomb-name">Energy Bomb</div><div class="bomb-desc">Energy damage, no block destruction</div></div>
    <div class="bomb-item"><div class="bomb-name">Dig Bomb</div><div class="bomb-desc">Tunnels straight down</div></div>
    <div class="bomb-item"><div class="bomb-name">Acid Liquid Bomb</div><div class="bomb-desc">Generates acid liquid</div></div>
    <div class="bomb-item"><div class="bomb-name">Water Liquid Bomb</div><div class="bomb-desc">Generates water</div></div>
    <div class="bomb-item"><div class="bomb-name">Lava Liquid Bomb</div><div class="bomb-desc">Generates lava</div></div>
  </div>
</div>

<!-- ==================== TOOLS PAGE ==================== -->
<div class="page" id="page-tools">
  <h1>Tools</h1>
  <p>Tools are essential for mining, digging, gardening, and creature catching. Higher tiers provide more mining power and faster operation.</p>

  <h2>Pickaxes</h2>
  <p>Primary mining tool. Higher power means faster mining and ability to break tougher blocks.</p>
  <table class="wiki-table">
    <thead><tr><th>Pickaxe</th><th>Power</th><th>Damage</th><th>Crafting</th><th>Notes</th></tr></thead>
    <tbody>
      <tr><td>Pickaxe</td><td>1.4</td><td>0.125</td><td>Wood + Iron Rubble</td><td>Starter tier</td></tr>
      <tr><td>Fine Pickaxe</td><td>1.9</td><td>0.175</td><td>Wood + Iron + Resin</td><td>&mdash;</td></tr>
      <tr><td>Diamond Pickaxe</td><td>2.35</td><td>0.225</td><td>Diamond tier materials</td><td>Requires diamond ore</td></tr>
      <tr><td>Onyx Pickaxe</td><td>2.75</td><td>0.275</td><td>Onyx tier materials</td><td>Requires onyx</td></tr>
      <tr><td>Platinum Pickaxe</td><td>2.75</td><td>0.275</td><td>Onyx Pickaxe + 100x Platinum Ore</td><td>Building 9. Highest tier</td></tr>
    </tbody>
  </table>

  <h2>Shovels</h2>
  <p>Dig through protected areas. Useful for accessing blocked-off sections.</p>
  <table class="wiki-table">
    <thead><tr><th>Shovel</th><th>Tier</th></tr></thead>
    <tbody>
      <tr><td>Shovel</td><td>Base</td></tr>
      <tr><td>Diamond Shovel</td><td>Diamond</td></tr>
      <tr><td>Onyx Shovel</td><td>Onyx</td></tr>
      <tr><td>Platinum Shovel</td><td>Platinum (highest)</td></tr>
    </tbody>
  </table>

  <h2>Spades</h2>
  <p>Used with the Horticulture skill. Spades recoup bulbs when mining flowers, allowing you to replant them.</p>
  <table class="wiki-table">
    <thead><tr><th>Spade</th><th>Tier</th></tr></thead>
    <tbody>
      <tr><td>Spade</td><td>Base</td></tr>
      <tr><td>Diamond Spade</td><td>Diamond</td></tr>
      <tr><td>Onyx Spade</td><td>Onyx</td></tr>
      <tr><td>Platinum Spade</td><td>Platinum (highest)</td></tr>
    </tbody>
  </table>

  <h2>Nets</h2>
  <p>Used to catch butterflies and insects. Higher-tier nets increase catch success rate.</p>
  <table class="wiki-table">
    <thead><tr><th>Net</th><th>Tier</th></tr></thead>
    <tbody>
      <tr><td>Net</td><td>Base</td></tr>
      <tr><td>Diamond Net</td><td>Diamond</td></tr>
      <tr><td>Onyx Net</td><td>Onyx</td></tr>
      <tr><td>Platinum Net</td><td>Platinum (highest)</td></tr>
    </tbody>
  </table>
</div>

<!-- ==================== ITEMS PAGE ==================== -->
<div class="page" id="page-items">
  <h1>Items & Resources</h1>
  <p>A comprehensive list of resources, ores, crystals, and other items found throughout Deepworld.</p>

  <h2>Ores</h2>
  <table class="wiki-table">
    <thead><tr><th>Ore</th><th>Rarity</th><th>Found In</th><th>Uses</th></tr></thead>
    <tbody>
      <tr><td>Copper</td><td>Common</td><td>Near surface, all biomes</td><td>Copper blocks, crafted into Brass</td></tr>
      <tr><td>Iron</td><td>Common</td><td>All biomes</td><td>Weapons, tools, crafting</td></tr>
      <tr><td>Zinc</td><td>Common</td><td>All biomes</td><td>Combined with Copper to make Brass</td></tr>
      <tr><td>Quartz</td><td>Moderate</td><td>All biomes</td><td>Tesla Club, Butler Bots</td></tr>
      <tr><td class="rarity-rare">Diamond</td><td>Rare</td><td>Arctic only</td><td>Diamond-tier tools, weapons, kits</td></tr>
      <tr><td class="rarity-rare">Beryllium</td><td>Rare</td><td>Desert only</td><td>Energy weapons, upgrade kits</td></tr>
      <tr><td class="rarity-epic">Onyx</td><td>Super Rare</td><td>Any biome (100% in Arctic)</td><td>Onyx-tier gear, currency</td></tr>
      <tr><td class="rarity-legendary">Platinum</td><td>Very Rare</td><td>Space only</td><td>Platinum-tier tools</td></tr>
      <tr><td>Bloodstone</td><td>Rare</td><td>Hell biome</td><td>Special crafting, figurines</td></tr>
      <tr><td>Marble</td><td>Rare</td><td>Various</td><td>Special crafting, figurines</td></tr>
    </tbody>
  </table>

  <h2>Processed Materials</h2>
  <table class="wiki-table">
    <thead><tr><th>Material</th><th>Source</th><th>Uses</th></tr></thead>
    <tbody>
      <tr><td>Brass</td><td>Copper + Zinc (smelting)</td><td>Weapons, machines, accessories</td></tr>
      <tr><td>Wood</td><td>Trees</td><td>Basic building, tool handles</td></tr>
      <tr><td>Resin</td><td>Trees (byproduct)</td><td>Fine-tier crafting</td></tr>
      <tr><td>Iron Rubble</td><td>Mining iron deposits</td><td>Basic tools, Sledgehammer</td></tr>
      <tr><td>Brass Rubble</td><td>Automata loot</td><td>Crafting</td></tr>
      <tr><td>Compost</td><td>Composter (earth + guano)</td><td>Growing plants</td></tr>
      <tr><td>Ectoplasm</td><td>Large Automata, ghosts</td><td>Special crafting</td></tr>
    </tbody>
  </table>

  <h2>Crystals</h2>
  <table class="wiki-table">
    <thead><tr><th>Crystal</th><th>Color</th><th>Found In</th><th>Uses</th></tr></thead>
    <tbody>
      <tr><td style="color:#44dd44">Green Crystal</td><td>Green</td><td>Temperate biome</td><td>Various crafting</td></tr>
      <tr><td style="color:#6ab8ff">Blue Crystal</td><td>Blue</td><td>Arctic biome</td><td>Steam weapons, items</td></tr>
      <tr><td style="color:#dddd44">Yellow Crystal</td><td>Yellow</td><td>Desert biome</td><td>Various crafting</td></tr>
      <tr><td style="color:#ff6644">Red Crystal</td><td>Red</td><td>Various</td><td>Weapons (fire, frost, acid, energy)</td></tr>
      <tr><td style="color:#cc88ff">Purple Crystal</td><td>Purple</td><td>Various</td><td>Butler Bots, advanced crafting</td></tr>
      <tr><td style="color:#ffffff">White Crystal</td><td>White</td><td>Various</td><td>Protector crafting</td></tr>
    </tbody>
  </table>

  <h2>Mushrooms</h2>
  <table class="wiki-table">
    <thead><tr><th>Mushroom</th><th>Biome</th></tr></thead>
    <tbody>
      <tr><td>Portabella</td><td>Temperate, Desert, Arctic</td></tr>
      <tr><td>Oyster</td><td>Temperate, Desert, Arctic</td></tr>
      <tr><td>Porcini</td><td>Temperate, Desert, Arctic</td></tr>
      <tr><td>Willow</td><td>Temperate</td></tr>
      <tr><td>Amanita</td><td>Temperate</td></tr>
      <tr><td>Chanterelle</td><td>Temperate, Desert, Arctic</td></tr>
      <tr><td>Morel</td><td>Temperate, Desert</td></tr>
      <tr><td>Acid Mushroom</td><td>Temperate, Desert</td></tr>
      <tr><td>Anbaric Mushroom</td><td>Desert</td></tr>
      <tr><td>Arctic Mushroom</td><td>Arctic</td></tr>
    </tbody>
  </table>

  <h2>Consumables</h2>
  <table class="wiki-table">
    <thead><tr><th>Item</th><th>Effect</th><th>Source</th></tr></thead>
    <tbody>
      <tr><td>Jar of Water</td><td>Restores hydration (Desert)</td><td>Fill jar at water source</td></tr>
      <tr><td>Jar of Acid</td><td>Acid Cannon ingredient</td><td>Collect from acid pools</td></tr>
      <tr><td>Jerky</td><td>Restores HP</td><td>Survival 2 crafting</td></tr>
      <tr><td>Power Jerky</td><td>Enhanced HP restoration</td><td>Survival 3 crafting</td></tr>
      <tr><td>Canister</td><td>Restores steam</td><td>Loot from containers, mobs</td></tr>
      <tr><td>Brainwine</td><td>Special consumable</td><td>Wine Press</td></tr>
    </tbody>
  </table>

  <h2>Containers</h2>
  <table class="wiki-table">
    <thead><tr><th>Container</th><th>Notes</th></tr></thead>
    <tbody>
      <tr><td>Chest / Large Chest</td><td>Standard storage</td></tr>
      <tr><td>Industrial Chest</td><td>Industrial-themed storage</td></tr>
      <tr><td>Mechanical Chest / Mechanical Large Chest</td><td>Found in dungeon airships</td></tr>
      <tr><td>Barrel / Tall Barrel / Windowed Barrel</td><td>Various barrel types</td></tr>
      <tr><td>Sack / Small Sack / Large Sack</td><td>Sack storage</td></tr>
      <tr><td>Crate / Small Crate / Large Crate / Industrial Crate</td><td>Green crates contain Purifier parts</td></tr>
      <tr><td>Chest of Plenty / Sack of Plenty</td><td>Premium loot containers</td></tr>
      <tr><td>Pandora Box</td><td>Special reward pools, spawns Dire Adult Brain</td></tr>
    </tbody>
  </table>

  <h2>Keys</h2>
  <div class="key-grid">
    <div class="key-item"><div class="key-name">Standard Key</div><div class="key-desc">Opens locked chests and standard locked containers found throughout the world.</div></div>
    <div class="key-item"><div class="key-name">Clown Key</div><div class="key-desc">Opens clown-themed containers with unique cosmetic and novelty loot.</div></div>
    <div class="key-item"><div class="key-name">Lizard Key</div><div class="key-desc">Opens lizard-themed containers with special reptilian-themed rewards.</div></div>
    <div class="key-item"><div class="key-name">Skeleton Key</div><div class="key-desc">Opens skeleton-themed containers with rare bone-related items and loot.</div></div>
  </div>

  <h2>Currency</h2>
  <table class="wiki-table">
    <thead><tr><th>Currency</th><th>Use</th><th>Source</th></tr></thead>
    <tbody>
      <tr><td>Crowns</td><td>Standard currency for purchases</td><td>Trading, shops</td></tr>
      <tr><td class="rarity-epic">Onyx</td><td>Rare currency for valuable items</td><td>Mining (rare)</td></tr>
      <tr><td class="rarity-legendary">Shillings</td><td>Android trading currency (Barter skill)</td><td>Brain kills, loot</td></tr>
    </tbody>
  </table>

  <h2>Other Items</h2>
  <table class="wiki-table">
    <thead><tr><th>Item</th><th>Description</th></tr></thead>
    <tbody>
      <tr><td>Schematic</td><td>Required for advanced crafting recipes</td></tr>
      <tr><td>Lockpick</td><td>Opens locked containers without a key</td></tr>
      <tr><td>Auctioneer's Gavel</td><td>Consumable to auction worlds to other players</td></tr>
      <tr><td>Android Figurine</td><td>Can be enlarged using Shillings + marble/bloodstone</td></tr>
      <tr><td>Guano</td><td>Combined with earth in Composter to make compost</td></tr>
    </tbody>
  </table>
</div>

<!-- ==================== SKILLS PAGE ==================== -->
<div class="page" id="page-skills">
  <h1>Skills</h1>
  <p>Deepworld has 11 skills that define your character's abilities. Each skill can be leveled up to improve its effects. Without Premium, the max skill level is 3.</p>

  <div class="skill-grid">
    <div class="skill-card">
      <div class="card-header">1. Agility</div>
      <div class="card-body">
        <p>Faster movement, climbing, and swimming. Higher jumps, reduced physical damage, longer stealth cloak duration.</p>
        <p><strong>Accessories:</strong> Brass Boot (+1), Diamond Boot (+2), Onyx Boot (+3)</p>
      </div>
    </div>
    <div class="skill-card">
      <div class="card-header">2. Barter</div>
      <div class="card-body">
        <p>Trading with androids using Shillings. Enables access to Barter Androids and improved trade deals. The higher the Barter level, the better deals you receive.</p>
        <p><strong>Currency:</strong> Shillings (obtained from Brain kills)</p>
      </div>
    </div>
    <div class="skill-card">
      <div class="card-header">3. Building</div>
      <div class="card-body">
        <p>Craft better items and place blocks farther away. Essential for base building and crafting progression.</p>
        <p><strong>Accessories:</strong> T-Square</p>
      </div>
    </div>
    <div class="skill-card">
      <div class="card-header">4. Combat</div>
      <div class="card-body">
        <p>Gun efficiency, critical hit rate, and bomb damage. Improves overall weapon effectiveness in combat.</p>
        <p><strong>Accessories:</strong> Brass Scope (+1), Diamond Scope (+2), Onyx Scope (+3)</p>
      </div>
    </div>
    <div class="skill-card">
      <div class="card-header">5. Engineering</div>
      <div class="card-body">
        <p>Craft advanced weapons and devices. Use steam more efficiently. Required for elemental weapons and machines.</p>
        <p><strong>Accessories:</strong> Sprocket, Widget</p>
      </div>
    </div>
    <div class="skill-card">
      <div class="card-header">6. Horticulture</div>
      <div class="card-body">
        <p>Plant bulbs and reclaim bulbs when mining flowers using a Spade. Enables farming and flower cultivation.</p>
        <p><strong>Accessories:</strong> Rake (+1), Diamond Rake (+2), Onyx Rake (+3)</p>
      </div>
    </div>
    <div class="skill-card">
      <div class="card-header">7. Luck</div>
      <div class="card-body">
        <p>Better loot quality and quantity from crates, chests, and containers. Increases rare drop chances.</p>
        <p><strong>Accessories:</strong> Clover (+1), Horseshoe (+2), Rabbit Foot (+3)</p>
      </div>
    </div>
    <div class="skill-card">
      <div class="card-header">8. Mining</div>
      <div class="card-body">
        <p>Mine faster and deeper. Level 2 unlocks deeper layers, Level 4 unlocks more block types.</p>
        <p><strong>Accessories:</strong> Mining Glove (+1), Diamond Glove (+2), Onyx Glove (+3)</p>
      </div>
    </div>
    <div class="skill-card">
      <div class="card-header">9. Perception</div>
      <div class="card-body">
        <p>Map abilities and zoom. L2: See teleporters on map. L3: See explored areas. L4+: Zoom out further.</p>
        <p><strong>Accessories:</strong> Stopwatch (+1), Pocketwatch (+2), Onyx Pocketwatch (+3)</p>
      </div>
    </div>
    <div class="skill-card">
      <div class="card-header">10. Stamina</div>
      <div class="card-body">
        <p>Increases max HP and unlocks additional accessory slots. More stamina = more survivability.</p>
        <p><strong>Accessories:</strong> Seashell (+1), Sand Dollar (+2), Conch (+3)</p>
      </div>
    </div>
    <div class="skill-card">
      <div class="card-header">11. Survival</div>
      <div class="card-body">
        <p>Reduced acid and fire damage. L2: Craft Jerky. L3: Craft Power Jerky. Essential for hostile biomes.</p>
        <p><strong>Accessories:</strong> Army Knife (+1), Diamond Army Knife (+2), Onyx Army Knife (+3)</p>
      </div>
    </div>
  </div>
</div>

<!-- ==================== ACCESSORIES PAGE ==================== -->
<div class="page" id="page-accessories">
  <h1>Accessories</h1>
  <p>Accessories are equippable items that boost skills, provide utilities, or grant special abilities. Accessory slots are limited by Stamina level.</p>

  <h2>Skill Boosters</h2>
  <p>Each skill has accessories that provide +1, +2, or +3 bonus levels to that skill.</p>
  <table class="wiki-table">
    <thead><tr><th>Skill</th><th>+1</th><th>+2</th><th>+3</th></tr></thead>
    <tbody>
      <tr><td>Agility</td><td>Brass Boot</td><td>Diamond Boot</td><td>Onyx Boot</td></tr>
      <tr><td>Combat</td><td>Brass Scope</td><td>Diamond Scope</td><td>Onyx Scope</td></tr>
      <tr><td>Horticulture</td><td>Rake</td><td>Diamond Rake</td><td>Onyx Rake</td></tr>
      <tr><td>Luck</td><td>Clover</td><td>Horseshoe</td><td>Rabbit Foot</td></tr>
      <tr><td>Mining</td><td>Mining Glove</td><td>Diamond Glove</td><td>Onyx Glove</td></tr>
      <tr><td>Perception</td><td>Stopwatch</td><td>Pocketwatch</td><td>Onyx Pocketwatch</td></tr>
      <tr><td>Stamina</td><td>Seashell</td><td>Sand Dollar</td><td>Conch</td></tr>
      <tr><td>Survival</td><td>Army Knife</td><td>Diamond Army Knife</td><td>Onyx Army Knife</td></tr>
      <tr><td>Building</td><td colspan="3">T-Square</td></tr>
      <tr><td>Engineering</td><td colspan="3">Sprocket, Widget</td></tr>
    </tbody>
  </table>

  <h2>Utility Accessories</h2>
  <div class="acc-grid">
    <div class="acc-item">
      <div class="acc-name">Steampack (Jetpack)</div>
      <div class="acc-desc">Enables flight. Tiers: Base, Brass (+10%), Diamond, Onyx</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Compressor</div>
      <div class="acc-desc">Increases total steam capacity. Tiers: Basic, Standard, Onyx</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Flashlight</div>
      <div class="acc-desc">Provides lighting in dark areas. Tiers: Brass, Diamond, Onyx</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Exo-skin</div>
      <div class="acc-desc">Environmental immunity &mdash; protects from acid rain, magma, and cold</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Breathing Apparatus</div>
      <div class="acc-desc">Unlimited breath underwater</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Afterburner</div>
      <div class="acc-desc">Enhanced flight speed and maneuverability</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Aquapack</div>
      <div class="acc-desc">Underwater mobility. Tiers: Brass, Diamond, Onyx</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Battery</div>
      <div class="acc-desc">Powers Butler Bots for extended operation</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Lockpick</div>
      <div class="acc-desc">Opens locked containers without keys</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Dowsing Rod</div>
      <div class="acc-desc">Locates nearby resources and ores underground</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Toolbelt</div>
      <div class="acc-desc">Extra accessory slots (purchase)</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Building Extender</div>
      <div class="acc-desc">Extended building placement range</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Butler Extender</div>
      <div class="acc-desc">Extended Butler Bot operational range</div>
    </div>
    <div class="acc-item">
      <div class="acc-name">Makeup Kit</div>
      <div class="acc-desc">Character customization options (purchase)</div>
    </div>
  </div>
</div>

<!-- ==================== MACHINES PAGE ==================== -->
<div class="page" id="page-machines">
  <h1>Machines & Structures</h1>
  <p>Machines are advanced devices that provide special functionality. Most require finding parts scattered throughout the world.</p>

  <h2>World Machines</h2>
  <div class="machine-grid">
    <div class="card">
      <div class="card-header">Purifier</div>
      <div class="card-body">
        <p>Assembled from 8 parts found in green crates. Purifies the world by stopping acid rain. After activation, rain becomes normal and flowers/plants can grow.</p>
        <p><strong>Parts:</strong> 8 unique components scattered in green Industrial Crates</p>
      </div>
    </div>
    <div class="card">
      <div class="card-header">Composter</div>
      <div class="card-body">
        <p>Combines earth + guano to produce compost. Compost is used for growing plants and flowers.</p>
        <p><strong>Parts:</strong> Found in the world</p>
      </div>
    </div>
    <div class="card">
      <div class="card-header">Recycler</div>
      <div class="card-body">
        <p>Breaks down items into their base materials. Useful for reclaiming resources from unwanted items.</p>
      </div>
    </div>
    <div class="card">
      <div class="card-header">Expiator</div>
      <div class="card-body">
        <p>Hell biome exclusive machine. Assembled from 8 parts, similar to the Purifier. Releases ghosts and affects the biome's supernatural activity.</p>
        <p><strong>Location:</strong> Hell biome only</p>
      </div>
    </div>
  </div>

  <h2>Teleportation</h2>
  <div class="machine-grid">
    <div class="card">
      <div class="card-header">Teleporter</div>
      <div class="card-body">
        <p>6 per world, found in dungeons as unrepaired units. Once repaired, they enable fast travel between teleporter locations.</p>
        <p><strong>Limit:</strong> Cannot place within 50 blocks of other teleporters</p>
      </div>
    </div>
    <div class="card">
      <div class="card-header">Target Teleporter</div>
      <div class="card-body">
        <p>Directional teleporter that sends the player to a specific Beacon location.</p>
      </div>
    </div>
    <div class="card">
      <div class="card-header">Beacon</div>
      <div class="card-body">
        <p>Named target for the Target Teleporter. Place at a destination and link to a Target Teleporter.</p>
      </div>
    </div>
    <div class="card">
      <div class="card-header">Portals</div>
      <div class="card-body">
        <p><strong>Orange Portal:</strong> Transports to a different server/world (costs 40 crowns)<br>
        <strong>Blue Portal:</strong> Transports within the same world</p>
      </div>
    </div>
  </div>

  <h2>Butler Bots</h2>
  <table class="wiki-table">
    <thead><tr><th>Bot</th><th>Recipe</th><th>Skill</th><th>Notes</th></tr></thead>
    <tbody>
      <tr><td>Brass Butler Bot</td><td>20x Brass Reinforced + 10x Quartz Ore + 2x Purple Crystal + Schematic</td><td>Building 4</td><td>Base tier helper bot</td></tr>
      <tr><td>Diamond Butler Bot</td><td>&mdash;</td><td>&mdash;</td><td>Higher tier</td></tr>
      <tr><td>Onyx Butler Bot</td><td>&mdash;</td><td>&mdash;</td><td>Highest tier, can transport magma</td></tr>
    </tbody>
  </table>

  <h2>Turrets</h2>
  <p>Craftable defensive weapons. Can be upgraded with Diamond and Onyx Turret Kits (MK1 &rarr; MK2 &rarr; MK3).</p>

  <h2>Crafting Stations</h2>
  <div class="acc-grid">
    <div class="acc-item"><div class="acc-name">Forge</div><div class="acc-desc">Smelting and metalworking</div></div>
    <div class="acc-item"><div class="acc-name">Furnace</div><div class="acc-desc">Heating and processing</div></div>
    <div class="acc-item"><div class="acc-name">Lathe</div><div class="acc-desc">Precision part crafting</div></div>
    <div class="acc-item"><div class="acc-name">Loom</div><div class="acc-desc">Textile and fabric crafting</div></div>
    <div class="acc-item"><div class="acc-name">Wine Press</div><div class="acc-desc">Makes Brainwine</div></div>
    <div class="acc-item"><div class="acc-name">Tesla Coil</div><div class="acc-desc">Mini-tesla energy device</div></div>
  </div>

  <h2>Protectors</h2>
  <p>The only way to prevent other players from mining your structures. Available as Micro Protector (tiny range) and Small Protector (larger range). Craftable with Engineering 13. Tradeable if level 20+ or premium.</p>
</div>

<!-- ==================== DUNGEONS PAGE ==================== -->
<div class="page" id="page-dungeons">
  <h1>Bunkers & Dungeons</h1>
  <p>Underground structures containing loot, enemies, and machine parts. Multi-looting allows anyone within 5 seconds to loot the same containers.</p>

  <h2>Bunkers</h2>
  <p>Abandoned underground shelters containing resources and sparkling barrels/crates with loot.</p>

  <div class="card">
    <div class="card-header">Standard Bunker</div>
    <div class="card-body">
      <p>Found in most biomes. Contains basic resources and sparkling barrels/crates that yield loot when opened. A good source of early-game materials and equipment.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">Ice Sculpture Bunker</div>
    <div class="card-body">
      <img class="wiki-img" src="https://static.wikia.nocookie.net/deepworld/images/f/f8/Screenshot_2025-10-29_004627.png" alt="Ice Sculpture Bunker" style="max-width:400px" onerror="this.style.display='none'">
      <p>Found exclusively in Arctic biomes. Contains ice sculptures along with standard bunker loot. The ice sculptures are unique decorative items.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">Present / Candy Cane Bunker</div>
    <div class="card-body">
      <p>Found exclusively in Arctic biomes. Contains candy canes, presents, and unique seasonal loot items not found elsewhere.</p>
    </div>
  </div>

  <h2>Dungeons</h2>
  <p>Dungeons are structured areas containing Brain and Automata enemies, turrets, spikes, and valuable loot. End rewards include machine parts and unrepaired teleporters.</p>

  <div class="card">
    <div class="card-header">Standard Dungeon</div>
    <div class="card-body">
      <p>Contains Brains, Automata, turrets, and spike traps. Loot chests are scattered throughout with progressively better rewards deeper in. Machine parts and teleporter components can be found as end rewards.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">Airship Dungeon</div>
    <div class="card-body">
      <img class="wiki-img" src="https://static.wikia.nocookie.net/deepworld/images/c/c1/Screenshot_2025-10-29_135953.png" alt="Airship Dungeon" style="max-width:400px" onerror="this.style.display='none'">
      <p>Sky-based dungeons found in the upper atmosphere. Feature spinning rotors, mechanical obstacles, and Mechanical Chests as the primary loot source. No safes are present in airship dungeons.</p>
      <img class="wiki-img" src="https://static.wikia.nocookie.net/deepworld/images/9/9b/Screenshot_2025-10-29_141404.png" alt="Airship" style="max-width:400px" onerror="this.style.display='none'">
    </div>
  </div>

  <div class="card">
    <div class="card-header">Pandora Encounter</div>
    <div class="card-body">
      <p>A special encounter triggered by opening a Pandora Box. Spawns a Dire Adult Brain (18 HP, Energy 0.5 damage, 30 XP). Rewards include special loot pools with Shillings (30) and unique items.</p>
    </div>
  </div>

  <h2>Airship Types</h2>
  <table class="wiki-table">
    <thead><tr><th>Type</th><th>Loot</th><th>Features</th></tr></thead>
    <tbody>
      <tr><td>Dungeon Airship</td><td>Mechanical Chests</td><td>Main dungeon loot, spinning rotors, no safes</td></tr>
      <tr><td>Red Chest Airship</td><td>Jerky, canisters, cosmetics</td><td>Red chest rewards</td></tr>
      <tr><td>Non-Red Chest Airship</td><td>Barrels, crates, basic resources</td><td>Standard container loot</td></tr>
    </tbody>
  </table>
</div>

<!-- ==================== GUIDE PAGE ==================== -->
<div class="page" id="page-guide">
  <h1>Gameplay Guide</h1>
  <p>A comprehensive guide to getting started and progressing in Deepworld.</p>

  <div class="guide-step">
    <h3>Getting Started</h3>
    <p>When you first enter Deepworld, you'll spawn in a Temperate biome world. Your first priorities should be:</p>
    <ul style="margin-left:18px;margin-bottom:8px;">
      <li>Craft a basic <strong>Pickaxe</strong> (Wood + Iron Rubble) to begin mining</li>
      <li>Gather <strong>Wood</strong> from trees and <strong>Iron Rubble</strong> from surface deposits</li>
      <li>Build a basic shelter to store items</li>
      <li>Craft a <strong>Sledgehammer</strong> (Wood + 2x Iron Rubble) for fighting mechanical enemies</li>
    </ul>
  </div>

  <div class="guide-step">
    <h3>Leveling & Skills</h3>
    <p>XP is earned by killing mobs, mining, and completing activities. As you level up, you gain skill points to invest in 11 skills. Key early skills:</p>
    <ul style="margin-left:18px;margin-bottom:8px;">
      <li><strong>Mining</strong> &mdash; Mine faster and access deeper layers</li>
      <li><strong>Building</strong> &mdash; Craft better items and weapons</li>
      <li><strong>Stamina</strong> &mdash; More HP and accessory slots</li>
      <li><strong>Engineering</strong> &mdash; Unlock elemental weapons</li>
    </ul>
    <p>Without Premium, max skill level is 3.</p>
  </div>

  <div class="guide-step">
    <h3>Crafting Progression</h3>
    <p>Crafting follows a tier system:</p>
    <ol style="margin-left:18px;margin-bottom:8px;">
      <li><strong>Base tier:</strong> Iron, Wood, basic materials</li>
      <li><strong>Fine tier:</strong> Iron + Resin upgrades</li>
      <li><strong>Diamond tier:</strong> Diamond ore from Arctic biomes</li>
      <li><strong>Onyx tier:</strong> Onyx ore (rare, 100% in Arctic)</li>
      <li><strong>Platinum tier:</strong> Platinum ore from Space biome (highest)</li>
    </ol>
    <p>Gun Parts (Gun Barrel, Pistol Stock, Musket Stock) must be crafted before assembling ranged weapons.</p>
  </div>

  <div class="guide-step">
    <h3>Exploration</h3>
    <p>Each biome has unique resources, enemies, and mechanics:</p>
    <ul style="margin-left:18px;margin-bottom:8px;">
      <li><strong>Temperate:</strong> Safe starting zone; find Purifier parts in green crates</li>
      <li><strong>Desert:</strong> Beryllium (exclusive); bring Jars of Water for hydration</li>
      <li><strong>Arctic:</strong> Diamonds + 100% Onyx; bring Exo-skin for cold protection</li>
      <li><strong>Hell:</strong> Bloodstone; Expiator machine; Skeleton Terrapus</li>
      <li><strong>Space:</strong> Platinum (exclusive); highest-tier tool materials</li>
    </ul>
  </div>

  <div class="guide-step">
    <h3>Building & Protection</h3>
    <p>Use blocks to build structures. Protectors (Micro and Small) prevent other players from mining your builds. Craftable at Engineering 13. Place protectors strategically to cover your base.</p>
  </div>

  <div class="guide-step">
    <h3>Currency & Trading</h3>
    <ul style="margin-left:18px;margin-bottom:8px;">
      <li><strong>Crowns:</strong> Standard currency used in shops and trading</li>
      <li><strong>Onyx:</strong> Rare currency for high-value trades</li>
      <li><strong>Shillings:</strong> Earned from Brain kills; used for Android trading (Barter skill)</li>
    </ul>
  </div>

  <div class="guide-step">
    <h3>PvP & Combat</h3>
    <p>Combat uses different damage types. Match your weapon to enemy weaknesses:</p>
    <ul style="margin-left:18px;margin-bottom:8px;">
      <li><strong>Slashing</strong> (Rapiers, Hatchets) &rarr; effective vs organic mobs (Terrapi)</li>
      <li><strong>Bludgeoning</strong> (Sledgehammers) &rarr; effective vs mechanical mobs (Automata)</li>
      <li><strong>Elemental</strong> (Fire, Frost, Acid, Energy) &rarr; use opposing elements for weakness exploitation</li>
    </ul>
    <p>The Combat skill increases gun efficiency, critical hit rate, and bomb damage.</p>
  </div>

  <div class="guide-step">
    <h3>Advanced Tips</h3>
    <ul style="margin-left:18px;margin-bottom:8px;">
      <li>Visit the same Android for 5 consecutive days for a special bonus item</li>
      <li>Use Dig Bombs to quickly tunnel downward</li>
      <li>The Dowsing Rod accessory helps locate underground resources</li>
      <li>Recycler machines can break down items to reclaim materials</li>
      <li>Blue Portals allow intra-world teleportation; Orange Portals go between worlds</li>
      <li>Multiple players can loot the same container if they access it within 5 seconds</li>
    </ul>
  </div>
</div>

<!-- ==================== COMMUNITY PAGE ==================== -->
<div class="page" id="page-community">
  <h1>Community</h1>

  <div class="card">
    <div class="card-header">History</div>
    <div class="card-body">
      <p>Deepworld was developed by <strong>Bytebin</strong> and launched in 2012 as a 2D sandbox crafting MMO. The game was available on iOS and Steam, gaining a dedicated community of players who enjoyed its unique steampunk-post-apocalyptic setting, crafting system, and multiplayer exploration.</p>
      <p>In 2019, the original servers were shut down, ending the official era of Deepworld.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">Closure & Revival</div>
    <div class="card-body">
      <p>After the official shutdown, the community refused to let the game die:</p>
      <ul style="margin-left:18px;margin-bottom:8px;">
        <li><strong>Brainwine</strong> &mdash; An open-source private server created by the community (<a href="https://github.com/kuroppoi/brainwine" target="_blank">github.com/kuroppoi/brainwine</a>)</li>
        <li><strong>Community Revival Server</strong> &mdash; A new server project with a custom Windows client, bringing modern features and quality-of-life improvements</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header">How to Play</div>
    <div class="card-body">
      <p>The original Steam page still exists, but the official servers are offline. To play Deepworld today:</p>
      <ol style="margin-left:18px;margin-bottom:8px;">
        <li>Join the <a href="https://discord.gg/deepworld" target="_blank">Deepworld Discord</a> for the latest server information</li>
        <li>Download the community client from the Discord</li>
        <li>Connect to the community revival server</li>
      </ol>
    </div>
  </div>

  <div class="card">
    <div class="card-header">Join the Community</div>
    <div class="card-body">
      <a href="https://discord.gg/deepworld" target="_blank" class="discord-btn">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.317 4.37a19.791 19.791 0 00-4.885-1.515.074.074 0 00-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 00-5.487 0 12.64 12.64 0 00-.617-1.25.077.077 0 00-.079-.037A19.736 19.736 0 003.677 4.37a.07.07 0 00-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 00.031.057 19.9 19.9 0 005.993 3.03.078.078 0 00.084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 00-.041-.106 13.107 13.107 0 01-1.872-.892.077.077 0 01-.008-.128 10.2 10.2 0 00.372-.292.074.074 0 01.077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 01.078.01c.12.098.246.198.373.292a.077.077 0 01-.006.127 12.299 12.299 0 01-1.873.892.077.077 0 00-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 00.084.028 19.839 19.839 0 006.002-3.03.077.077 0 00.032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 00-.031-.03z"/></svg>
        Join the Deepworld Discord
      </a>
      <p style="margin-top:10px;">The Discord server is the primary hub for:</p>
      <ul style="margin-left:18px;">
        <li>Server status and announcements</li>
        <li>Client downloads and setup help</li>
        <li>Trading and marketplace</li>
        <li>Community events and guides</li>
        <li>Bug reports and suggestions</li>
      </ul>
    </div>
  </div>
</div>

<!-- ==================== CATALOG PAGE ==================== -->
<div class="page" id="page-catalog">
  <h1>Sprite Catalog</h1>
  <p>The complete Deepworld sprite sheet containing all game items, blocks, mobs, and objects. Use the zoom controls to inspect individual sprites.</p>

  <div class="zoom-controls">
    <button class="zoom-btn" onclick="zoomSprite(-1)">&#8722; Zoom Out</button>
    <button class="zoom-btn" onclick="zoomSprite(1)">&#43; Zoom In</button>
    <button class="zoom-btn" onclick="zoomSprite(0)">Reset</button>
    <span id="zoomLevel" style="color:var(--text-dim);font-size:13px;line-height:32px;margin-left:8px;">100%</span>
  </div>
  <div class="sprite-viewer" id="spriteViewer">
    <img src="assets/sprite.jpg" alt="Deepworld Sprite Sheet" id="spriteImg" style="width:100%;">
  </div>
  <p class="wiki-img-caption">Full Deepworld sprite sheet &mdash; contains all items, blocks, mobs, and objects used in the game.</p>
</div>

</main>

<!-- ===== BACK TO TOP ===== -->
<button class="back-to-top" id="backToTop" onclick="window.scrollTo({top:0,behavior:'smooth'})">&#9650;</button>

<!-- ===== JAVASCRIPT ===== -->
<script>
// ===== Hash Router =====
const pages = ['home','biomes','mobs','weapons','tools','items','skills','accessories','machines','dungeons','guide','community','catalog'];

function navigate(hash) {
  const page = hash.replace('#','') || 'home';
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  const target = document.getElementById('page-' + page);
  if (target) {
    target.classList.add('active');
  } else {
    document.getElementById('page-home').classList.add('active');
  }
  // Update active nav
  document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
  const activeLink = document.querySelector('.nav-link[data-page="'+page+'"]');
  if (activeLink) activeLink.classList.add('active');
  // Scroll to top
  window.scrollTo(0,0);
  // Close mobile sidebar
  document.getElementById('sidebar').classList.remove('open');
  document.getElementById('sidebarOverlay').classList.remove('active');
}

window.addEventListener('hashchange', () => navigate(location.hash));
window.addEventListener('DOMContentLoaded', () => navigate(location.hash || '#home'));

// ===== Sidebar Toggle =====
function toggleSidebar() {
  const sb = document.getElementById('sidebar');
  const ov = document.getElementById('sidebarOverlay');
  sb.classList.toggle('open');
  ov.classList.toggle('active');
}

// ===== Back to Top =====
window.addEventListener('scroll', () => {
  const btn = document.getElementById('backToTop');
  if (window.scrollY > 300) btn.classList.add('visible');
  else btn.classList.remove('visible');
});

// ===== Sprite Zoom =====
let spriteZoom = 100;
function zoomSprite(dir) {
  if (dir === 0) spriteZoom = 100;
  else if (dir > 0) spriteZoom = Math.min(spriteZoom + 50, 500);
  else spriteZoom = Math.max(spriteZoom - 50, 50);
  document.getElementById('spriteImg').style.width = spriteZoom + '%';
  document.getElementById('zoomLevel').textContent = spriteZoom + '%';
}

// ===== Search =====
const searchIndex = [
  {title:'Home', page:'home', tags:'home welcome start'},
  {title:'Biomes', page:'biomes', tags:'biomes temperate desert arctic hell deep brain space'},
  {title:'Temperate Biome', page:'biomes', tags:'temperate acid rain green crystal mushroom purifier'},
  {title:'Desert Biome', page:'biomes', tags:'desert dehydration beryllium scorpion sand worm armadillo'},
  {title:'Arctic Biome', page:'biomes', tags:'arctic ice cold diamond onyx frost'},
  {title:'Hell Biome', page:'biomes', tags:'hell fire skeleton terrapus expiator bloodstone'},
  {title:'Deep Biome', page:'biomes', tags:'deep underground darkness'},
  {title:'Brain Biome', page:'biomes', tags:'brain baby homeland'},
  {title:'Space Biome', page:'biomes', tags:'space platinum christmas'},
  {title:'Mobs & Creatures', page:'mobs', tags:'mobs creatures enemies'},
  {title:'Terrapus', page:'mobs', tags:'terrapus juvenile adult fire acid skeleton frost queen pet'},
  {title:'Brains', page:'mobs', tags:'brain tiny juvenile adult dire brain lord energy'},
  {title:'Automata', page:'mobs', tags:'automata mechanical walker flyer small medium large'},
  {title:'Supernatural', page:'mobs', tags:'ghost revenant dire revenant lord shadow'},
  {title:'Desert Creatures', page:'mobs', tags:'scorpion sand worm armadillo'},
  {title:'Androids', page:'mobs', tags:'android barter shillings trade'},
  {title:'Pets', page:'mobs', tags:'pet terrapus crow bunny skunk vulture automata cat dog'},
  {title:'Weapons & Combat', page:'weapons', tags:'weapons combat ranged melee guns'},
  {title:'Gun Parts', page:'weapons', tags:'gun barrel pistol stock musket stock'},
  {title:'Weapon Upgrade Kits', page:'weapons', tags:'diamond weapon kit onyx weapon kit upgrade mk2 mk3'},
  {title:'Pistol', page:'weapons', tags:'pistol piercing ranged'},
  {title:'Musket', page:'weapons', tags:'musket piercing ranged'},
  {title:'Steam Pistol', page:'weapons', tags:'steam pistol fire'},
  {title:'Steam Cannon', page:'weapons', tags:'steam cannon fire'},
  {title:'Flame Pistol', page:'weapons', tags:'flame pistol fire'},
  {title:'Flamethrower', page:'weapons', tags:'flamethrower fire'},
  {title:'Frost Pistol', page:'weapons', tags:'frost pistol cold'},
  {title:'Frost Cannon', page:'weapons', tags:'frost cannon cold'},
  {title:'Acid Cannon', page:'weapons', tags:'acid cannon'},
  {title:'Energy Pistol', page:'weapons', tags:'energy pistol'},
  {title:'Energy Cannon', page:'weapons', tags:'energy cannon'},
  {title:'Sledgehammer', page:'weapons', tags:'sledgehammer bludgeoning melee'},
  {title:'Rapier', page:'weapons', tags:'rapier slashing melee'},
  {title:'Hatchet', page:'weapons', tags:'hatchet slashing melee'},
  {title:'Tesla Club', page:'weapons', tags:'tesla club energy melee'},
  {title:'Cane', page:'weapons', tags:'cane bludgeoning melee'},
  {title:'Bombs', page:'weapons', tags:'bomb big mega mine fire energy dig liquid'},
  {title:'Tools', page:'tools', tags:'tools pickaxe shovel spade net'},
  {title:'Pickaxes', page:'tools', tags:'pickaxe fine diamond onyx platinum mining'},
  {title:'Shovels', page:'tools', tags:'shovel diamond onyx platinum digging'},
  {title:'Spades', page:'tools', tags:'spade diamond onyx platinum horticulture'},
  {title:'Nets', page:'tools', tags:'net diamond onyx platinum butterfly catching'},
  {title:'Items & Resources', page:'items', tags:'items resources ores crystals'},
  {title:'Ores', page:'items', tags:'copper iron zinc quartz diamond beryllium onyx platinum bloodstone marble'},
  {title:'Crystals', page:'items', tags:'green blue yellow red purple white crystal'},
  {title:'Mushrooms', page:'items', tags:'mushroom portabella oyster porcini willow amanita chanterelle morel acid anbaric arctic'},
  {title:'Consumables', page:'items', tags:'jar water acid jerky power jerky canister brainwine'},
  {title:'Containers', page:'items', tags:'chest barrel sack crate mechanical pandora'},
  {title:'Keys', page:'items', tags:'key standard clown lizard skeleton'},
  {title:'Currency', page:'items', tags:'crowns onyx shillings currency'},
  {title:'Skills', page:'skills', tags:'skills agility barter building combat engineering horticulture luck mining perception stamina survival'},
  {title:'Agility', page:'skills', tags:'agility movement jumping swimming stealth'},
  {title:'Barter', page:'skills', tags:'barter trading android shillings'},
  {title:'Building', page:'skills', tags:'building craft place blocks'},
  {title:'Combat', page:'skills', tags:'combat gun critical bomb'},
  {title:'Engineering', page:'skills', tags:'engineering weapons devices steam'},
  {title:'Horticulture', page:'skills', tags:'horticulture plant bulb flower spade'},
  {title:'Luck', page:'skills', tags:'luck loot quality'},
  {title:'Mining', page:'skills', tags:'mining mine faster deeper'},
  {title:'Perception', page:'skills', tags:'perception map zoom teleporter'},
  {title:'Stamina', page:'skills', tags:'stamina hp accessory slots'},
  {title:'Survival', page:'skills', tags:'survival acid fire resist jerky'},
  {title:'Accessories', page:'accessories', tags:'accessories skill booster utility steampack compressor flashlight'},
  {title:'Steampack', page:'accessories', tags:'steampack jetpack flight'},
  {title:'Exo-skin', page:'accessories', tags:'exo-skin exoskin acid magma cold immunity'},
  {title:'Machines & Structures', page:'machines', tags:'machines structures purifier composter recycler expiator'},
  {title:'Purifier', page:'machines', tags:'purifier acid rain parts green crate'},
  {title:'Composter', page:'machines', tags:'composter earth guano compost'},
  {title:'Recycler', page:'machines', tags:'recycler break down items materials'},
  {title:'Expiator', page:'machines', tags:'expiator hell ghost'},
  {title:'Teleporter', page:'machines', tags:'teleporter fast travel portal beacon'},
  {title:'Butler Bots', page:'machines', tags:'butler bot brass diamond onyx'},
  {title:'Turrets', page:'machines', tags:'turret defense upgrade kit'},
  {title:'Protectors', page:'machines', tags:'protector micro small protection mining'},
  {title:'Bunkers & Dungeons', page:'dungeons', tags:'bunker dungeon airship pandora'},
  {title:'Standard Bunker', page:'dungeons', tags:'standard bunker resources loot'},
  {title:'Ice Sculpture Bunker', page:'dungeons', tags:'ice sculpture bunker arctic'},
  {title:'Present Bunker', page:'dungeons', tags:'present candy cane bunker arctic'},
  {title:'Standard Dungeon', page:'dungeons', tags:'standard dungeon brain automata turret spike'},
  {title:'Airship Dungeon', page:'dungeons', tags:'airship dungeon mechanical chest rotor'},
  {title:'Pandora Encounter', page:'dungeons', tags:'pandora encounter dire brain'},
  {title:'Gameplay Guide', page:'guide', tags:'guide getting started leveling crafting exploration building'},
  {title:'Community', page:'community', tags:'community history closure revival discord brainwine'},
  {title:'Sprite Catalog', page:'catalog', tags:'sprite catalog sheet items zoom'},
];

function handleSearch() {
  const q = document.getElementById('searchInput').value.toLowerCase().trim();
  const dd = document.getElementById('searchDropdown');
  if (!q) { dd.classList.remove('active'); return; }
  const results = searchIndex.filter(e =>
    e.title.toLowerCase().includes(q) || e.tags.includes(q)
  ).slice(0, 10);
  if (results.length === 0) {
    dd.innerHTML = '<div class="search-result-item"><span class="sr-title">No results</span></div>';
  } else {
    dd.innerHTML = results.map(r =>
      '<div class="search-result-item" onclick="location.hash=\'#'+r.page+'\';document.getElementById(\'searchInput\').value=\'\';document.getElementById(\'searchDropdown\').classList.remove(\'active\');">' +
      '<div class="sr-title">'+r.title+'</div>' +
      '<div class="sr-section">'+r.page+'</div></div>'
    ).join('');
  }
  dd.classList.add('active');
}

// Close search on click outside
document.addEventListener('click', (e) => {
  if (!e.target.closest('.search-box')) {
    document.getElementById('searchDropdown').classList.remove('active');
  }
});
</script>

</body>
</html>
'''

with open('/home/user/workspace/deepworld-wiki/index.html', 'w') as f:
    f.write(html)

print(f"Written {len(html)} bytes to index.html")
