// Copyright (c) 2023, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('Attendance', {
// fetch location if want to update on attentence based on chceking field fetch_current_location
fetch_current_location:function(frm){


        if(frm.doc.fetch_current_location==1){
            console.log('haii')

        function onPositionRecieved(position){
            var longitude= position.coords.longitude;
            var latitude= position.coords.latitude;
            frm.set_value('longitude',longitude);
            frm.set_value('latitude',latitude);
            console.log(longitude);
            console.log(latitude);
            fetch('https://api.opencagedata.com/geocode/v1/json?q='+latitude+'+'+longitude+'&key=de1bf3be66b546b89645e500ec3a3a28')
             .then(response => response.json())
              .then(data => {
                var city;

                if (data['results'][0].components.city) {
                    city = data['results'][0].components.city;
                } else if (data['results'][0].components.town) {
                    city = data['results'][0].components.town;
                } else if (data['results'][0].components.village) {
                    city = data['results'][0].components.village;
                } else if (data['results'][0].components.suburb) {
                    city = data['results'][0].components.suburb;
                } else if (data['results'][0].components.road) {
                    city = data['results'][0].components.road;
                } else if (data['results'][0].components.highway) {
                    city = data['results'][0].components.highway;
                } 
                  var state=data['results'][0].components.state;
                  var area=data['results'][0].formatted;
                  frm.set_value('city',city);
                  frm.set_value('state',state);
                  frm.set_value('area',area);
                  console.log(data);
              })
              .catch(err => console.log(err));
            frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+latitude+','+longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
              frm.refresh_field('my_location');
        }
        
        function locationNotRecieved(positionError){
            console.log(positionError);
        }
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition(onPositionRecieved,locationNotRecieved,{ enableHighAccuracy: true});
        }

    }
},

//fetch location on load automatically only if lat and long is empty in current form.

onload:function(frm){
        console.log("onload works")
        if(frm.doc.fetch_current_location==0){
            frm.set_value(frm.doc.fetch_current_location,1);
            frm.refresh_field('frm.doc.fetch_current_locations');
        }

        function onPositionRecieved(position){
            var longitude= position.coords.longitude;
            var latitude= position.coords.latitude;
            frm.set_value('longitude',longitude);
            frm.set_value('latitude',latitude);
            console.log(longitude);
            console.log(latitude);
            fetch('https://api.opencagedata.com/geocode/v1/json?q='+latitude+'+'+longitude+'&key=de1bf3be66b546b89645e500ec3a3a28')
             .then(response => response.json())
              .then(data => {
                var city;
                if (data['results'][0].components.city) {
                    city = data['results'][0].components.city;
                } else if (data['results'][0].components.town) {
                    city = data['results'][0].components.town;
                } else if (data['results'][0].components.village) {
                    city = data['results'][0].components.village;
                } else if (data['results'][0].components.suburb) {
                    city = data['results'][0].components.suburb;
                } else if (data['results'][0].components.road) {
                    city = data['results'][0].components.road;
                } else if (data['results'][0].components.highway) {
                    city = data['results'][0].components.highway;
                } 


                console.log(city,"city")
                console.log(data,"data")
                  var state=data['results'][0].components.state;
                  var area=data['results'][0].formatted;
                  frm.set_value('city',city);
                  frm.set_value('state',state);
                  frm.set_value('area',area);
                  console.log(data);
              })
              .catch(err => console.log(err));
            frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+latitude+','+longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
              frm.refresh_field('my_location');
        }
        
        function locationNotRecieved(positionError){
            console.log(positionError);
        }
        
        if(frm.doc.longitude && frm.doc.latitude){
            frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+frm.doc.latitude+','+frm.doc.longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
              frm.refresh_field('my_location');
        } else {
            if(navigator.geolocation){
                navigator.geolocation.getCurrentPosition(onPositionRecieved,locationNotRecieved,{ enableHighAccuracy: true});
            }
        }


    },
     

    
});
