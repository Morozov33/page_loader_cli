(function(e) {
    e.fn.hoverIntent = function(t, n, r) {
        var i = {
            interval: 100,
            sensitivity: 7,
            timeout: 0
        };
        if (typeof t === "object") {
            i = e.extend(i, t)
        } else if (e.isFunction(n)) {
            i = e.extend(i, {
                over: t,
                out: n,
                selector: r
            })
        } else {
            i = e.extend(i, {
                over: t,
                out: t,
                selector: n
            })
        }
        var s, o, u, a;
        var f = function(e) {
            s = e.pageX;
            o = e.pageY
        };
        var l = function(t, n) {
            n.hoverIntent_t = clearTimeout(n.hoverIntent_t);
            if (Math.abs(u - s) + Math.abs(a - o) < i.sensitivity) {
                e(n).off("mousemove.hoverIntent", f);
                n.hoverIntent_s = 1;
                return i.over.apply(n, [t])
            } else {
                u = s;
                a = o;
                n.hoverIntent_t = setTimeout(function() {
                    l(t, n)
                }, i.interval)
            }
        };
        var c = function(e, t) {
            t.hoverIntent_t = clearTimeout(t.hoverIntent_t);
            t.hoverIntent_s = 0;
            return i.out.apply(t, [e])
        };
        var h = function(t) {
            var n = jQuery.extend({}, t);
            var r = this;
            if (r.hoverIntent_t) {
                r.hoverIntent_t = clearTimeout(r.hoverIntent_t)
            }
            if (t.type == "mouseenter") {
                u = n.pageX;
                a = n.pageY;
                e(r).on("mousemove.hoverIntent", f);
                if (r.hoverIntent_s != 1) {
                    r.hoverIntent_t = setTimeout(function() {
                        l(n, r)
                    }, i.interval)
                }
            } else {
                e(r).off("mousemove.hoverIntent", f);
                if (r.hoverIntent_s == 1) {
                    r.hoverIntent_t = setTimeout(function() {
                        c(n, r)
                    }, i.timeout)
                }
            }
        };
        return this.on({
            "mouseenter.hoverIntent": h,
            "mouseleave.hoverIntent": h
        }, i.selector)
    }
})(jQuery);
jQuery.easing['jswing'] = jQuery.easing['swing'];
jQuery.extend(jQuery.easing, {
    def: 'easeOutQuad',
    swing: function(x, t, b, c, d) {
        return jQuery.easing[jQuery.easing.def](x, t, b, c, d)
    },
    easeInQuad: function(x, t, b, c, d) {
        return c * (t /= d) * t + b
    },
    easeOutQuad: function(x, t, b, c, d) {
        return -c * (t /= d) * (t - 2) + b
    },
    easeInOutQuad: function(x, t, b, c, d) {
        if ((t /= d / 2) < 1) return c / 2 * t * t + b;
        return -c / 2 * ((--t) * (t - 2) - 1) + b
    },
    easeInCubic: function(x, t, b, c, d) {
        return c * (t /= d) * t * t + b
    },
    easeOutCubic: function(x, t, b, c, d) {
        return c * ((t = t / d - 1) * t * t + 1) + b
    },
    easeInOutCubic: function(x, t, b, c, d) {
        if ((t /= d / 2) < 1) return c / 2 * t * t * t + b;
        return c / 2 * ((t -= 2) * t * t + 2) + b
    },
    easeInQuart: function(x, t, b, c, d) {
        return c * (t /= d) * t * t * t + b
    },
    easeOutQuart: function(x, t, b, c, d) {
        return -c * ((t = t / d - 1) * t * t * t - 1) + b
    },
    easeInOutQuart: function(x, t, b, c, d) {
        if ((t /= d / 2) < 1) return c / 2 * t * t * t * t + b;
        return -c / 2 * ((t -= 2) * t * t * t - 2) + b
    },
    easeInQuint: function(x, t, b, c, d) {
        return c * (t /= d) * t * t * t * t + b
    },
    easeOutQuint: function(x, t, b, c, d) {
        return c * ((t = t / d - 1) * t * t * t * t + 1) + b
    },
    easeInOutQuint: function(x, t, b, c, d) {
        if ((t /= d / 2) < 1) return c / 2 * t * t * t * t * t + b;
        return c / 2 * ((t -= 2) * t * t * t * t + 2) + b
    },
    easeInSine: function(x, t, b, c, d) {
        return -c * Math.cos(t / d * (Math.PI / 2)) + c + b
    },
    easeOutSine: function(x, t, b, c, d) {
        return c * Math.sin(t / d * (Math.PI / 2)) + b
    },
    easeInOutSine: function(x, t, b, c, d) {
        return -c / 2 * (Math.cos(Math.PI * t / d) - 1) + b
    },
    easeInExpo: function(x, t, b, c, d) {
        return (t == 0) ? b : c * Math.pow(2, 10 * (t / d - 1)) + b
    },
    easeOutExpo: function(x, t, b, c, d) {
        return (t == d) ? b + c : c * (-Math.pow(2, -10 * t / d) + 1) + b
    },
    easeInOutExpo: function(x, t, b, c, d) {
        if (t == 0) return b;
        if (t == d) return b + c;
        if ((t /= d / 2) < 1) return c / 2 * Math.pow(2, 10 * (t - 1)) + b;
        return c / 2 * (-Math.pow(2, -10 * --t) + 2) + b
    },
    easeInCirc: function(x, t, b, c, d) {
        return -c * (Math.sqrt(1 - (t /= d) * t) - 1) + b
    },
    easeOutCirc: function(x, t, b, c, d) {
        return c * Math.sqrt(1 - (t = t / d - 1) * t) + b
    },
    easeInOutCirc: function(x, t, b, c, d) {
        if ((t /= d / 2) < 1) return -c / 2 * (Math.sqrt(1 - t * t) - 1) + b;
        return c / 2 * (Math.sqrt(1 - (t -= 2) * t) + 1) + b
    },
    easeInElastic: function(x, t, b, c, d) {
        var s = 1.70158;
        var p = 0;
        var a = c;
        if (t == 0) return b;
        if ((t /= d) == 1) return b + c;
        if (!p) p = d * .3;
        if (a < Math.abs(c)) {
            a = c;
            var s = p / 4
        } else var s = p / (2 * Math.PI) * Math.asin(c / a);
        return -(a * Math.pow(2, 10 * (t -= 1)) * Math.sin((t * d - s) * (2 * Math.PI) / p)) + b
    },
    easeOutElastic: function(x, t, b, c, d) {
        var s = 1.70158;
        var p = 0;
        var a = c;
        if (t == 0) return b;
        if ((t /= d) == 1) return b + c;
        if (!p) p = d * .3;
        if (a < Math.abs(c)) {
            a = c;
            var s = p / 4
        } else var s = p / (2 * Math.PI) * Math.asin(c / a);
        return a * Math.pow(2, -10 * t) * Math.sin((t * d - s) * (2 * Math.PI) / p) + c + b
    },
    easeInOutElastic: function(x, t, b, c, d) {
        var s = 1.70158;
        var p = 0;
        var a = c;
        if (t == 0) return b;
        if ((t /= d / 2) == 2) return b + c;
        if (!p) p = d * (.3 * 1.5);
        if (a < Math.abs(c)) {
            a = c;
            var s = p / 4
        } else var s = p / (2 * Math.PI) * Math.asin(c / a);
        if (t < 1) return -.5 * (a * Math.pow(2, 10 * (t -= 1)) * Math.sin((t * d - s) * (2 * Math.PI) / p)) + b;
        return a * Math.pow(2, -10 * (t -= 1)) * Math.sin((t * d - s) * (2 * Math.PI) / p) * .5 + c + b
    },
    easeInBack: function(x, t, b, c, d, s) {
        if (s == undefined) s = 1.70158;
        return c * (t /= d) * t * ((s + 1) * t - s) + b
    },
    easeOutBack: function(x, t, b, c, d, s) {
        if (s == undefined) s = 1.70158;
        return c * ((t = t / d - 1) * t * ((s + 1) * t + s) + 1) + b
    },
    easeInOutBack: function(x, t, b, c, d, s) {
        if (s == undefined) s = 1.70158;
        if ((t /= d / 2) < 1) return c / 2 * (t * t * (((s *= (1.525)) + 1) * t - s)) + b;
        return c / 2 * ((t -= 2) * t * (((s *= (1.525)) + 1) * t + s) + 2) + b
    },
    easeInBounce: function(x, t, b, c, d) {
        return c - jQuery.easing.easeOutBounce(x, d - t, 0, c, d) + b
    },
    easeOutBounce: function(x, t, b, c, d) {
        if ((t /= d) < (1 / 2.75)) {
            return c * (7.5625 * t * t) + b
        } else if (t < (2 / 2.75)) {
            return c * (7.5625 * (t -= (1.5 / 2.75)) * t + .75) + b
        } else if (t < (2.5 / 2.75)) {
            return c * (7.5625 * (t -= (2.25 / 2.75)) * t + .9375) + b
        } else {
            return c * (7.5625 * (t -= (2.625 / 2.75)) * t + .984375) + b
        }
    },
    easeInOutBounce: function(x, t, b, c, d) {
        if (t < d / 2) return jQuery.easing.easeInBounce(x, t * 2, 0, c, d) * .5 + b;
        return jQuery.easing.easeOutBounce(x, t * 2 - d, 0, c, d) * .5 + c * .5 + b
    }
});
(function(a) {
    a.fn.extend({
        actual: function(b, k) {
            var c, d, h, g, f, j, e, i;
            if (!this[b]) {
                throw '$.actual => The jQuery method "' + b + '" you called does not exist'
            }
            h = a.extend({
                absolute: false,
                clone: false,
                includeMargin: undefined
            }, k);
            d = this;
            if (h.clone === true) {
                e = function() {
                    d = d.filter(":first").clone().css({
                        position: "absolute",
                        top: -1000
                    }).appendTo("body")
                };
                i = function() {
                    d.remove()
                }
            } else {
                e = function() {
                    c = d.parents().andSelf().filter(":hidden");
                    g = h.absolute === true ? {
                        position: "absolute",
                        visibility: "hidden",
                        display: "block"
                    } : {
                        visibility: "hidden",
                        display: "block"
                    };
                    f = [];
                    c.each(function() {
                        var m = {},
                            l;
                        for (l in g) {
                            m[l] = this.style[l];
                            this.style[l] = g[l]
                        }
                        f.push(m)
                    })
                };
                i = function() {
                    c.each(function(m) {
                        var n = f[m],
                            l;
                        for (l in g) {
                            this.style[l] = n[l]
                        }
                    })
                }
            }
            e();
            j = /(outer)/g.test(b) ? d[b](h.includeMargin) : d[b]();
            i();
            return j
        }
    })
})(jQuery);
$('li,a', '.sidebox ul.cat-tree').removeAttr('id').removeAttr('ondblclick').removeAttr('class');
$('.sidebox ul.cat-tree li,.sidebox .gTable').each(function() {
    var $this = $(this);
    $this.html($this.html().replace(/&nbsp;/g, ''))
});
$('.sidebox ul.cat-tree:first').addClass('ut-menu ut-vmenu');
$('.sidebox ul.cat-tree').removeAttr('style').removeClass('cat-tree');
var sw = window.innerWidth;
breakpoint = 959,
    mobile = false;
$('#catmenu').prepend('<div class="nav-head"><div class="icon"><span></span><span></span><span></span><span></span></div></div>');
if (sw < breakpoint) {
    $('#catmenu').attr('class', 'nav-mobi')
}
$(function($) {
    function $ulight(parent, url, hlclass) {
        var ls = $(parent).find("a").get(),
            o = null,
            l = 0;
        for (var j in ls) {
            if (ls[j].href && url.indexOf(ls[j].href) >= 0) {
                if (!o || l < ls[j].href.length) {
                    o = ls[j];
                    l = ls[j].href.length
                }
            }
        }
        if (o) $(o).addClass(hlclass)
    }
    $ulight($('#catmenu')[0], document.location.href + '/', 'current-item');
    $('#catmenu > div > ul').hover(function() {
        $('#catmenu ul li a.current-item').addClass('no-bg')
    }, function() {
        $('#catmenu ul li a.current-item').removeClass('no-bg')
    });
    var parentLi = $('#catmenu ul li:has(ul)').addClass('item-parent');
    if (!$('#catmenu').hasClass('nav-mobi')) {
        var config = {
            interval: 0,
            over: function() {
                if (mobile) return;
                $(this).addClass('hover');
                $('> ul', this).animate({
                    visibility: 'toggle',
                    opacity: 'toggle'
                }, 0);
                $('> a', this).addClass('current-item');
                $('#catmenu ul li a.current-item').addClass('no-bd')
            },
            timeout: 100,
            out: function() {
                if (mobile) return;
                $(this).removeClass('hover');
                $('> ul', this).animate({
                    opacity: 'toggle',
                    visibility: 'toggle'
                }, 0);
                $('> a', this).removeClass('current-item');
                $('#catmenu ul li a.current-item').removeClass('no-bd')
            }
        };
        parentLi.hoverIntent(config)
    }

    function nav_transform() {
        if (!mobile) {
            $('#catmenu').removeAttr('class');
            $('#catmenu > div > ul').show();
            return
        } else {
            $('#catmenu').attr('class', 'nav-mobi');
            if (!$('.nav-head').hasClass('over')) {
                $('#catmenu > div > ul').hide()
            }
        }
    }
    $(window).resize(function() {
        sw = window.innerWidth;
        mobile = (sw > breakpoint) ? false : true;
        nav_transform()
    });
    $('> a', parentLi).after('<i class="material-icons arrow-menu-icon">keyboard_arrow_down</i>');

    function changeMenuIcon() {
        if (window.innerWidth < 961) {
            $('#catmenu li.uWithSubmenu i').each(function() {
                $(this).html() == 'keyboard_arrow_down' && $(this).html('add');
            });
        } else {
            $('#catmenu li.uWithSubmenu i').html('keyboard_arrow_down');
        }
    };

    changeMenuIcon();
    $(window).resize(function() {
        changeMenuIcon();
    });

    $('> i', parentLi).click(function() {
        if ($(this).text() == 'add') {
            $(this).parent().addClass('over');
            $(this).next().show();
            $(this).text('remove')
        } else if ($(this).text() == 'remove') {
            $(this).parent().removeClass('over');
            $(this).next().hide();
            $(this).text('add')
        }
        return false
    });
    $('.nav-head').click(function() {
        $(this).toggleClass('over').next().children().toggle();
        return false
    })
});
$(function($) {
    var sdLi = $('.sidebox ul li:has(ul)').addClass('item-parent');
    $(sdLi).each(function() {
        $(this).prepend('<em>+</em>');
        $('em', this).css('top', $(this).actual('outerHeight') / 2 - $('em', this).actual('outerHeight') / 2)
    });
    $('> em', sdLi).click(function() {
        if ($(this).text() == '+') {
            $(this).parent().addClass('over');
            $(this).text('-');
        } else {
            $(this).parent().removeClass('over');
            $(this).text('+');
        }
    });
    var config = {
        interval: 0,
        over: function() {
            $(this).prev().addClass('hover')
        },
        timeout: 0,
        out: function() {
            $(this).prev().removeClass('hover')
        }
    };
    $('> a', sdLi).hoverIntent(config);
    $('.uTable').wrap('<div class="x-scroll"></div>');
});
$(window).on("load", function() {
    $(window).resize().scroll()
});
$('.site-n a').click(function(e) {
    if ($(e.target).hasClass('uz-signs')) {
        e.preventDefault()
    }
});

if ($('#cont-shop-invoices h1').length) {

    $('#cont-shop-invoices h1 + table')
        .addClass('status_table')
        .after('<div class="fil_togg_wrapper"><div class="fil_togg_holder"><span class="material-icons">storage</span><span class="material-icons arrow">keyboard_arrow_down</span></div></div>')
        .siblings('table, hr')
        .addClass('filter_table');
    var buttonToIcon = {
        '#invoice-form-export': 'file_download',
        '#invoice-form-print': 'print',
        '#invoice-form-send-el-goods': 'forward'

    }
    convertToIcon(buttonToIcon);
    $(document).ajaxComplete(function() {
        convertToIcon(buttonToIcon);
    });

    $('.fil_togg_holder').on('click', function() {
        var arrow = $(this).children('.arrow');
        $('.filter_table').fadeToggle();
        arrow.text(arrow.text() == 'keyboard_arrow_up' ? 'keyboard_arrow_down' : 'keyboard_arrow_up');
    });

    function convertToIcon(obj) {
        for (var prop in obj) {
            $(prop)
                .attr('title', $(prop).val())
                .addClass('material-icons')
                .val(obj[prop]);
        }
    }
}


if (currentPageIdTemplate == 'invoices' || currentPageIdTemplate == 'checkout' || currentModuleTemplate == 'forum') {
    $("table > tbody > tr > td").addClass('pageinvoices');
}
