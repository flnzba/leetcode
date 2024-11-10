# LeetCode Fortschritt

## Gesamtübersicht der gelösten Aufgaben

| Schwierigkeitsgrad | Anzahl gelöster Aufgaben |
| ------------------ | ------------------------ |
| Einfach            | 4                        |
| Mittel             | 0                        |
| Schwer             | 0                        |

## Detaillierte Statistiken

### Einfache Aufgaben
- [x] 1544. Make The String Great - [1544. Make The String Great](https://leetcode.com/problems/make-the-string-great/description/)
- [x] 1. Two Sum - [1. Two Sum](https://leetcode.com/problems/two-sum/description/)
- [x] 792. Rotate String - [792. Rotate String](https://leetcode.com/problems/rotate-string/description/)
- [x] 14. Longest Common Prefix - [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)

### Mittelschwere Aufgaben

---

### Schwere Aufgaben

---

## Leistungsbewertung

![Status Screenshot](https://github.com/user-attachments/assets/ac9d3cbd-8739-4eed-b9ce-a2e6d7cd1674)

## Tech
- Java
- Python
- Javascript

<div>
    <h1>Meine LeetCode Statistiken</h1>
    <div id="stats"></div>
    <script src="load_stats.js"></script>
</div>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    fetch('leetcode_stats.json')
        .then(response => response.json())
        .then(data => {
            const statsElement = document.getElementById('stats');
            statsElement.innerHTML = `
                <p>Gesamt gelöste Probleme: ${data.total_problems_solved}</p>
                <p>Leichte Probleme gelöst: ${data.easy_problems_solved}</p>
                <p>Mittel-schwere Probleme gelöst: ${data.medium_problems_solved}</p>
                <p>Schwere Probleme gelöst: ${data.hard_problems_solved}</p>
                <p>Gesamtpunktzahl: ${data.total_score}</p>
            `;
        })
        .catch(error => console.error('Fehler beim Laden der Daten:', error));
});
</script>
