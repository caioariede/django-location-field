!function($){
    $.locationField = function(options) {
        var LocationField = {
            options: $.extend({
                mapType: 'google',
                mapId: 'map',
                mapLatLng: '0,0',
                mapOptions: {
                    zoom: 9
                },
                basedFieldsSelector: [],
                suffix: '',
                fixMarker: true
            }, options),

            mapTypes: /google/,

            render: function() {
                if ( ! this.mapTypes.test(this.options.mapType)) {
                    console.error('invalid map type');
                }

                var mapOptions = this._getMapOptions(),
                    map = this._getMap(mapOptions);

                if (mapOptions.center) {
                    L.marker(mapOptions.center).addTo(map);
                }

                // fix issue w/ marker not appearing
                if (this.options.fixMarker)
                    this.__fixMarker();
            },

            _getMap: function(mapOptions) {
                var map = new L.Map(this.options.mapId, mapOptions);

                if (this.options.mapType == 'google') {
                    map.addLayer(new L.Google('ROADMAP'));
                }

                return map;
            },

            _getMapOptions: function() {
                return $.extend(this.options.mapOptions, {
                    center: this._getLatLng()
                });
            },

            _getLatLng: function() {
                var l = this.options.mapLatLng.split(',').map(parseFloat);
                return new L.LatLng(l[0], l[1]);
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
            mapId: $el.attr('data-map').replace(/^#/, ''),
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
        values.mapLatLng = latLng;
        values.mapOptions = {
            zoom: $el.attr('data-zoom')
        };

        $.locationField(values).render();

    });
}($ || django.jQuery);
