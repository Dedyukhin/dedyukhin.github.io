/**
 * Main JavaScript for Ivan Dedyukhin's Academic Website
 */

/**
 * Toggle abstract/details visibility for publications and teaching cards
 * @param {string} id - The ID of the element to toggle
 * @param {HTMLElement} btn - Optional button element for ARIA attributes
 */
function toggleAbstract(id, btn) {
    const el = document.getElementById(id);
    if (!el) return;

    const isHidden = el.style.display === "none" || el.style.display === "";

    if (isHidden) {
        el.style.display = "block";
        if (btn) btn.setAttribute('aria-expanded', 'true');
        el.scrollIntoView({ behavior: "smooth", block: "nearest" });
    } else {
        el.style.display = "none";
        if (btn) btn.setAttribute('aria-expanded', 'false');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });
});
