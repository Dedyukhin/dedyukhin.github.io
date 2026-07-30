/**
 * Ivan Dedyukhin - academic website
 *
 * Three small progressive enhancements, no dependencies:
 *   1. Disclosure controls (abstracts, student feedback)
 *   2. Compact navigation menu on small screens
 *   3. Copy-to-clipboard for the email address
 *
 * Every element this file touches is fully usable without JavaScript: the
 * disclosure panels render open and their triggers stay hidden until wired up
 * here, the navigation list is a plain visible list until collapsed here, and
 * the email address is plain selectable text with its "Copy" hint hidden.
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

    /* --------------------------------------------------------------------
       Copy to clipboard
       -------------------------------------------------------------------- */

    // Used when the async Clipboard API is unavailable (older browsers) or is
    // refused, which happens outside a secure context.
    function legacyCopy(text) {
        var field = document.createElement('textarea');
        var copied = false;

        field.value = text;
        field.setAttribute('readonly', '');
        field.style.position = 'fixed';
        field.style.top = '-1000px';
        field.style.opacity = '0';
        document.body.appendChild(field);
        field.select();

        try {
            copied = document.execCommand('copy');
        } catch (error) {
            copied = false;
        }

        document.body.removeChild(field);
        return copied;
    }

    function copyText(text) {
        if (navigator.clipboard && window.isSecureContext) {
            return navigator.clipboard.writeText(text).then(function () {
                return true;
            }, function () {
                return legacyCopy(text);
            });
        }
        return Promise.resolve(legacyCopy(text));
    }

    function initCopy() {
        var controls = document.querySelectorAll('[data-copy-text]');

        Array.prototype.forEach.call(controls, function (control) {
            var feedback = control.querySelector('[data-copy-feedback]') || control;
            var idle = feedback.textContent;
            var done = control.getAttribute('data-copy-done') || 'Copied';
            var timer;

            control.addEventListener('click', function () {
                copyText(control.getAttribute('data-copy-text')).then(function (copied) {
                    // On failure the address stays on screen to select by hand.
                    feedback.textContent = copied ? done : 'Select and copy';
                    control.setAttribute('data-copied', copied ? 'true' : 'false');

                    window.clearTimeout(timer);
                    timer = window.setTimeout(function () {
                        feedback.textContent = idle;
                        control.removeAttribute('data-copied');
                    }, 2500);
                });
            });
        });
    }

    function init() {
        initDisclosures();
        initNav();
        initCopy();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
}());
