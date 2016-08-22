(jQuery || django.jQuery)(function($){
    function location_field_load(map, location_based, zoom, suffix)
    {
        var parent = map.parent().parent();

        var location_map;

        var location_coordinate = parent.find('input[type=text]');

        function savePosition(point)
        {
            if (point) {
                location_coordinate.val(point.lat().toFixed(6) + "," + point.lng().toFixed(6));
                location_map.panTo(point);
            }
            else {
                var point = new google.maps.LatLng(1, 1);
                location_map.panTo(point)
            }
        }

        function load() {
            var point = new google.maps.LatLng(1, 1);

            var options = {
                mapTypeId: google.maps.MapTypeId.ROADMAP
            };
            
            location_map = new google.maps.Map(map[0], options);

            var initial_position;

            if (location_coordinate.val())
            {
                var l = location_coordinate.val().split(/,/);

                if (l.length > 1)
                {
                    initial_position = new google.maps.LatLng(l[0], l[1]);
                }
            }

            var marker = new google.maps.Marker({
                map: location_map,
                position: initial_position,
                draggable: true
            });

            google.maps.event.addListener(marker, 'dragend', function(mouseEvent) {
                savePosition(mouseEvent.latLng);
            });

            google.maps.event.addListener(location_map, 'click', function(mouseEvent){
                marker.setPosition(mouseEvent.latLng);
                savePosition(mouseEvent.latLng);
            });

            var no_change = false;

            location_based.each(function(i, f)
            {
                var f = $(this),
                    cb = function()
                    {
                        no_change = true;

                        var lstr = [];

                        location_based.each(function(){
                            var b = $(this);

                            if (b.is('select'))
                                lstr.push(b.find('option:selected').html());
                            else
                                lstr.push(b.val())
                        });

                        if (lstr.length > 0 && suffix != '') 
                            lstr.push(suffix);

                        geocode(lstr.join(','), function(l){
                            location_coordinate.val(l.lat()+','+l.lng());
                            setTimeout(function(){ no_change = false; }, 2000);
                        });
                    };

                if (f.is('select'))
                    f.change(cb);
                else
                    f.keyup(cb);
            });

            // Prevents querying Google Maps everytime field changes
            var location_coordinate_delay;

            location_coordinate.keyup(function(){
                if (no_change) return;
                var latlng = $(this).val().split(/,/);
                if (latlng.length < 2) return;
                clearTimeout(location_coordinate_delay);
                location_coordinate_delay = setTimeout(function(){
                    var ll = new google.maps.LatLng(latlng[0], latlng[1]);
                    location_map.panTo(ll);
                    marker.setPosition(ll);
                }, 1200);
            });

            function placeMarker(location) {
                location_map.setZoom(zoom);
                marker.setPosition(location);
                location_map.setCenter(location);
                savePosition(location);
            }

            function geocode(address, cb) {
                var result;
                var geocoder = new google.maps.Geocoder();
                if (geocoder) {
                    geocoder.geocode({"address": address}, function(results, status) {
                        if (status == google.maps.GeocoderStatus.OK) {
                            cb(results[0].geometry.location);
                            placeMarker(results[0].geometry.location);
                        }
                    });
                }
            }

            function geocode_reverse(location, cb) {
                var geocoder = new google.maps.Geocoder();
                if (geocoder) {
                    geocoder.geocode({"latLng": location}, function(results, status) {
                        if (status == google.maps.GeocoderStatus.OK) {
                            cb(results[0].geometry.location);
                            placeMarker(results[0].geometry.location);
                        }
                    });
                }
            }

            placeMarker(initial_position);
        }

        load();
    }


    $('input[data-location-widget]').livequery(function(){
        var $el = $(this), name = $el.attr('name'), pfx;

        try {
            pfx = name.match(/-(\d+)-/)[1];
        } catch (e) {};

        var values = {
            map: $el.attr('data-map'),
            zoom: $el.attr('data-zoom'),
            suffix: $el.attr('data-suffix'),
            based_fields: $el.attr('data-based-fields')
        }

        if ( ! /__prefix__/.test(name)) {
            for (key in values) {
                if (/__prefix__/.test(values[key])) {
                    values[key] = values[key].replace(/__prefix__/g, pfx);
                }
            }
        }

        var $map = $(values.map),
            $based_fields = $(values.based_fields),
            zoom = parseInt(values.zoom),
            suffix = values.suffix;

        location_field_load($map, $based_fields, zoom, suffix);
    });
});