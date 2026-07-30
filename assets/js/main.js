/**
 * Ivan Dedyukhin - academic website
 *
 * Two small progressive enhancements, no dependencies:
 *   1. Disclosure controls (abstracts, additional student feedback)
 *   2. Compact navigation menu on small screens
 *
 * Every element this file touches is fully usable without JavaScript: the
 * disclosure panels render open and their triggers stay hidden until wired up
 * here, and the navigation list is a plain visible list until collapsed here.
 */
(function () {
    'use strict';

    /* --------------------------------------------------------------------
       Disclosure controls
       -------------------------------------------------------------------- */
    function setDisclosure(trigger, panel, open) {
        trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
        panel.classList.toggle('is-open', open);
        if (open) {
            panel.removeAttribute('hidden');
        } else {
            panel.setAttribute('hidden', '');
        }
    }

    function initDisclosures() {
        var triggers = document.querySelectorAll('.disclosure-trigger[aria-controls]');

        Array.prototype.forEach.call(triggers, function (trigger) {
            var panel = document.getElementById(trigger.getAttribute('aria-controls'));
            if (!panel) {
                return;
            }

            // Collapse by default now that the control is available.
            setDisclosure(trigger, panel, trigger.getAttribute('aria-expanded') === 'true');

            trigger.addEventListener('click', function () {
                var isOpen = trigger.getAttribute('aria-expanded') === 'true';
                setDisclosure(trigger, panel, !isOpen);
            });
        });
    }

    /* --------------------------------------------------------------------
       Compact navigation
       -------------------------------------------------------------------- */
    function initNav() {
        var toggle = document.querySelector('.nav-toggle');
        if (!toggle) {
            return;
        }

        var list = document.getElementById(toggle.getAttribute('aria-controls'));
        if (!list) {
            return;
        }

        function close() {
            toggle.setAttribute('aria-expanded', 'false');
            list.classList.remove('is-open');
        }

        toggle.addEventListener('click', function () {
            var isOpen = toggle.getAttribute('aria-expanded') === 'true';
            toggle.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
            list.classList.toggle('is-open', !isOpen);
        });

        // Close on Escape, and after following a link on a small screen.
        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
                close();
                toggle.focus();
            }
        });

        Array.prototype.forEach.call(list.querySelectorAll('a'), function (link) {
            link.addEventListener('click', close);
        });

        // Reset state when the menu button is no longer displayed.
        if (window.matchMedia) {
            var wide = window.matchMedia('(min-width: 761px)');
            var onChange = function (event) {
                if (event.matches) {
                    close();
                }
            };
            if (wide.addEventListener) {
                wide.addEventListener('change', onChange);
            } else if (wide.addListener) {
                wide.addListener(onChange);
            }
        }
    }

    function init() {
        initDisclosures();
        initNav();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
}());
