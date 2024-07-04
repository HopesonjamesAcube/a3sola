frappe.listview_settings["Attendance"] = {
    onload: function (list_view) {
    list_view.page.add_inner_button(__("IN"), function () {
        
        // var longitude="NIL"
        // var latitude="NIL"

        function onPositionRecieved(position){
            var city="NIL"
            var area="NIL"
            var state="NIL"
            var longitude= position.coords.longitude;
            var latitude= position.coords.latitude;
            console.log(longitude);
            console.log(latitude);
            fetch('https://api.opencagedata.com/geocode/v1/json?q='+latitude+'+'+longitude+'&key=de1bf3be66b546b89645e500ec3a3a28')
             .then(response => response.json())
              .then(data => {
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


                // console.log(city,"city")
                // console.log(data['results'],"data")
                // console.log(data['results'][0],"data @0")
                // console.log(data['results'][0].components,"data components")
                // console.log(data['results'][0].components.city,"data, city")
                  state=data['results'][0].components.state;
                  area=data['results'][0].formatted;
                  console.log(data);
                //   console.log("///////")
                //   console.log("longitude",longitude,"latitude",)
                //   console.log(city,"citydown")
                //   console.log(city,state,area,longitude.latitude,"/////////////")
              frappe.call({
                method: "a3sola_solar_management.doc_events.attendance.markinattendance",
                args:{
                    city:city,
                    area:area,
                    state:state,
                    longitude:longitude,
                    latitude:latitude,
                },
                callback: function (r) {
                if (r.message) {
                    console.log(r,"%%%%%%%%%%%")
                frappe.msgprint(__("Attendance 'In' marked successfully"));
                // Optionally, you can refresh the list view to show the updated data.
                list_view.refresh();
                }
                },
                });
              })
              .catch(err => console.log(err));
              
        }
        
        function locationNotRecieved(positionError){
            console.log(positionError);
        }
        
            if(navigator.geolocation){
                console.log("navigator works")
                navigator.geolocation.getCurrentPosition(onPositionRecieved,locationNotRecieved,{ enableHighAccuracy: true});
            }

    
    }).addClass('btn-primary');
    list_view.page.add_inner_button(__("OUT"), function () {
        function onPositionRecieved(position){
            var city="NIL"
            var area="NIL"
            var state="NIL"
            var longitude= position.coords.longitude;
            var latitude= position.coords.latitude;
            console.log(longitude);
            console.log(latitude);
            fetch('https://api.opencagedata.com/geocode/v1/json?q='+latitude+'+'+longitude+'&key=de1bf3be66b546b89645e500ec3a3a28')
             .then(response => response.json())
              .then(data => {
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


                // console.log(city,"city")
                // console.log(data['results'],"data")
                // console.log(data['results'][0],"data @0")
                // console.log(data['results'][0].components,"data components")
                // console.log(data['results'][0].components.city,"data, city")
                  state=data['results'][0].components.state;
                  area=data['results'][0].formatted;
                  console.log(data);
                //   console.log("///////")
                //   console.log("longitude",longitude,"latitude",)
                //   console.log(city,"citydown")
                //   console.log(city,state,area,longitude.latitude,"/////////////")
              frappe.call({
                method: "a3sola_solar_management.doc_events.attendance.markoutattendance",
                args:{
                    city:city,
                    area:area,
                    state:state,
                    longitude:longitude,
                    latitude:latitude,
                },
                callback: function (r) {
                if (r.message) {
                    console.log(r,"%%%%%%%%%%%")
                frappe.msgprint(__("Attendance 'Out' marked successfully"));
                // Optionally, you can refresh the list view to show the updated data.
                list_view.refresh();
                }
                },
                });
              })
              .catch(err => console.log(err));
              
        }
        
        function locationNotRecieved(positionError){
            console.log(positionError);
        }
        
            if(navigator.geolocation){
                console.log("navigator works")
                navigator.geolocation.getCurrentPosition(onPositionRecieved,locationNotRecieved,{ enableHighAccuracy: true});
            }
    


    }).addClass('btn-primary');
    },
    };
    