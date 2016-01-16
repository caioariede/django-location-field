!function($){
    $.locationField = function(options) {
        var LocationField = {
            options: $.extend({
                type: 'google',
                id: 'map',
                latLng: '0,0',
                mapOptions: {
                    zoom: 9
                },
                basedFieldsSelector: [],
                suffix: '',
                fixMarker: true
            }, options),

            types: /google|openstreetmap|mapbox/,

            render: function() {
                if ( ! this.types.test(this.options.type)) {
                    console.error('invalid map type');
                }

                document.getElementById(this.options.id).innerHTML = 'Loading...';

                var self = this;

                this.load[this.options.type](function(){
                    var mapOptions = self._getMapOptions(),
                        map = self._getMap(mapOptions);
        
                    self._addMarker(map, mapOptions.center);

                    // fix issue w/ marker not appearing
                    if (self.options.type == 'google' && self.options.fixMarker)
                        self.__fixMarker();
                });
            },

            fill: function(latLng) {
                console.log(latLng);
            },

            load: {
                google: function(onload) {
                    var js = '//maps.google.com/maps/api/js?sensor=false',
                        self = this;

                    this._loadJS(js, function(){
                        self.leaflet(function(){
                            js = '//matchingnotes.com/javascripts/leaflet-google.js';
                            self._loadJS(js, onload);
                        });
                    });
                },

                mapbox: function(onload) {
                    this.leaflet(onload);
                },

                leaflet: function(onload) {
                    var self = this,
                        js = [
                            'http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js',
                        ],
                        css = 'http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css';

                    this._loadJSList(js, function(){
                        self._loadCSS(css, onload);
                    });
                },

                _loadJSList: function(srclist, onload) {
                    if (srclist.length > 1) {
                        var head = srclist.shift(),
                            self = this;

                        this._loadJS(head, function(){
                            self._loadJSList(srclist, onload);
                        });
                    }
                    else {
                        this._loadJS(srclist[0], onload);
                    }
                },

                _loadJS: function(src, onload) {
                    if (this.__loaded[src] != undefined) {
                        onload();
                    }
                    else {
                        this.__loaded[src] = 1;
                        var el = document.createElement('script');
                        el.type = 'application/javascript';
                        el.src = src;
                        el.onload = onload;
                        document.body.appendChild(el);
                    }
                },

                _loadCSS: function(src, onload) {
                    if (this.__loaded[src] != undefined) {
                        onload();
                    }
                    else {
                        this.__loaded[src] = 1;
                        onloadCSS(loadCSS(src), onload);
                    }
                },

                __loaded: {}
            },

            _getMap: function(mapOptions) {
                var map = new L.Map(this.options.id, mapOptions), layer;

                if (this.options.type == 'google') {
                    layer = new L.Google('ROADMAP');
                }
                else if (this.options.type == 'openstreetmap') {
                    layer = new L.tileLayer(
                        'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                            maxZoom: 18
                        });
                }
                else if (this.options.type == 'mapbox') {
                    layer = new L.tileLayer(
                        'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
                            maxZoom: 18,
                            accessToken: 'pk.eyJ1IjoibWFwYm94IiwiYSI6IjZjNmRjNzk3ZmE2MTcwOTEwMGY0MzU3YjUzOWFmNWZhIn0.Y8bhBaUMqFiPrDRW9hieoQ',
                            id: 'mapbox.streets'
                        });
                }

                map.addLayer(layer);

                return map;
            },

            _getMapOptions: function() {
                return $.extend(this.options.mapOptions, {
                    center: this._getLatLng()
                });
            },

            _getLatLng: function() {
                var l = this.options.latLng.split(',').map(parseFloat);
                return new L.LatLng(l[0], l[1]);
            },

            _addMarker: function(map, center) {
                var self = this,
                    markerOptions = {
                        draggable: true
                    };

                var marker = L.marker(center, markerOptions).addTo(map);

                // fill input on dragend
                marker.on('dragend move', function(){
                    self.fill(this.getLatLng());
                });

                // place marker on map click
                map.on('click', function(e){
                    marker.setLatLng(e.latlng);
                });
            },

            __fixMarker: function() {
                $('.leaflet-map-pane').css('z-index', '2 !important');
                $('.leaflet-google-layer').css('z-index', '1 !important');
            }
        }

        return {
            render: LocationField.render.bind(LocationField)
        }
    }

    $('input[data-location-widget]').livequery(function(){
        var $el = $(this), name = $el.attr('name'),
            latLng = $el.parent().find(':text').val() || '0,0',
            pfx;

        try {
            pfx = name.match(/-(\d+)-/)[1];
        } catch (e) {};

        var values = {
            id: $el.attr('data-map').replace(/^#/, ''),
            basedFieldsSelector: $el.attr('data-based-fields')
        }

        if ( ! /__prefix__/.test(name)) {
            for (key in values) {
                if (/__prefix__/.test(values[key])) {
                    values[key] = values[key].replace(/__prefix__/g, pfx);
                }
            }
        }

        values.suffix = $el.attr('data-suffix');
        values.latLng = latLng;
        values.type = $el.attr('data-map-type');
        values.mapOptions = {
            zoom: $el.attr('data-zoom')
        };

        $.locationField(values).render();

    });
}($ || django.jQuery);


/*!
loadCSS: load a CSS file asynchronously.
[c]2015 @scottjehl, Filament Group, Inc.
Licensed MIT
*/
(function(w){
	"use strict";
	/* exported loadCSS */
	var loadCSS = function( href, before, media ){
		// Arguments explained:
		// `href` [REQUIRED] is the URL for your CSS file.
		// `before` [OPTIONAL] is the element the script should use as a reference for injecting our stylesheet <link> before
			// By default, loadCSS attempts to inject the link after the last stylesheet or script in the DOM. However, you might desire a more specific location in your document.
		// `media` [OPTIONAL] is the media type or query of the stylesheet. By default it will be 'all'
		var doc = w.document;
		var ss = doc.createElement( "link" );
		var ref;
		if( before ){
			ref = before;
		}
		else {
			var refs = ( doc.body || doc.getElementsByTagName( "head" )[ 0 ] ).childNodes;
			ref = refs[ refs.length - 1];
		}

		var sheets = doc.styleSheets;
		ss.rel = "stylesheet";
		ss.href = href;
		// temporarily set media to something inapplicable to ensure it'll fetch without blocking render
		ss.media = "only x";

		// Inject link
			// Note: the ternary preserves the existing behavior of "before" argument, but we could choose to change the argument to "after" in a later release and standardize on ref.nextSibling for all refs
			// Note: `insertBefore` is used instead of `appendChild`, for safety re: http://www.paulirish.com/2011/surefire-dom-element-insertion/
		ref.parentNode.insertBefore( ss, ( before ? ref : ref.nextSibling ) );
		// A method (exposed on return object for external use) that mimics onload by polling until document.styleSheets until it includes the new sheet.
		var onloadcssdefined = function( cb ){
			var resolvedHref = ss.href;
			var i = sheets.length;
			while( i-- ){
				if( sheets[ i ].href === resolvedHref ){
					return cb();
				}
			}
			setTimeout(function() {
				onloadcssdefined( cb );
			});
		};

		// once loaded, set link's media back to `all` so that the stylesheet applies once it loads
		ss.onloadcssdefined = onloadcssdefined;
		onloadcssdefined(function() {
			ss.media = media || "all";
		});
		return ss;
	};
	// commonjs
	if( typeof module !== "undefined" ){
		module.exports = loadCSS;
	}
	else {
		w.loadCSS = loadCSS;
	}
}( typeof global !== "undefined" ? global : this ));


/*!
onloadCSS: adds onload support for asynchronous stylesheets loaded with loadCSS.
[c]2014 @zachleat, Filament Group, Inc.
Licensed MIT
*/

/* global navigator */
/* exported onloadCSS */
function onloadCSS( ss, callback ) {
	ss.onload = function() {
		ss.onload = null;
		if( callback ) {
			callback.call( ss );
		}
	};

	// This code is for browsers that don’t support onload, any browser that
	// supports onload should use that instead.
	// No support for onload:
	//	* Android 4.3 (Samsung Galaxy S4, Browserstack)
	//	* Android 4.2 Browser (Samsung Galaxy SIII Mini GT-I8200L)
	//	* Android 2.3 (Pantech Burst P9070)

	// Weak inference targets Android < 4.4
	if( "isApplicationInstalled" in navigator && "onloadcssdefined" in ss ) {
		ss.onloadcssdefined( callback );
	}
}
