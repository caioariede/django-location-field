function location_field_load(map, location_based, zoom)
{
    var parent = map.parent().parent();

    var location_map;

    var location_coordinate = parent.find('input[type=text]');

    function savePosition(point)
    {
        location_coordinate.val(point.lat().toFixed(6) + "," + point.lng().toFixed(6));
        location_map.panTo(point);
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
            var cb = function(){
                no_change = true;
                var lstr = [];
                location_based.each(function(a, b){
                    if (/select/i.test(b[0].tagName)) lstr.push(b.find('option:selected').html());
                    else lstr.push(b.val())
                })
                geocode(lstr.join(','), function(l){
                    location_coordinate.val(l.lat()+','+l.lng());
                    setTimeout(function(){ no_change = false; }, 2000);
                });
            };

            no_change = true;

            if (/select/i.test(f[0].tagName))
                f.change(cb);
            else f.keyup(cb);
        });

        location_coordinate.keyup(function(){
            if (no_change) return;
            var latlng = $(this).val().split(/,/);
            if (latlng.length < 2) return;
            var latlng = new google.maps.LatLng(latlng[0], latlng[1]);
            geocode_reverse(latlng, function(l){
                location_coordinate.val(l.lat()+','+l.lng());
            });
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
