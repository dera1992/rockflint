// variable that keeps all the filter information

var send_data = {}

$(document).ready(function () {
    appendFilters();

    $('#sort').on('change', function () {
        send_data['sort'] = this.value;
        getAPIData();
    });

    // display the results after reseting the filters

    $("#display_filterd").click(function(){
        event.preventDefault();
        console.log($(this).serialize());
        appendFilters();
        getAPIData();
    })
    // $("#list_data").submit(function(){
    //     event.preventDefault();
    //     var send_data = $(this).serialize();
    //     getAPIData();
    // })
})


/**
    Function that resets all the filters
**/
function appendFilters() {
    var title = $("#title").val();
    var property_tpe = $("#ptypes").val();
    var price_min = $("#price_min").val();
    var price_max = $("#price_max").val();
    var bedrooms = $("#bedrooms").val();
    var bathrooms = $("#bathrooms").val();
    var cities = $("#cities").val();
    var area_min = $("#area_min").val();
    var area_max = $("#area_max").val();
    var air_conditioning = $("#air_conditioning").val();
    var parking = $("#parking").val();
    var sewer = $("#sewer").val();
    var water = $("#water").val();
    var microwave = $("#microwave").val();
    var swimming_pool = $("#swimming_pool").val();
    var barbecue = $("#barbecue").val();
    var lawn = $("#lawn").val();
    var tv_cable = $("#tv_cable").val();
    var wi_fi = $("#wi_fi").val();
    var gym = $("#gym").val();
    var church = $("#church").val();
    var mosque = $("#mosque").val();
    var school = $("#school").val();
    var market = $("#market").val();
    var hospital = $("#hospital").val();
    var resturant = $("#resturant").val();
    var beach = $("#beach").val();



    send_data['title_contains_query'] = title;
    send_data["category"] = property_tpe;
    send_data["ad_price_min"] = price_min;
    send_data["ad_price_max"] = price_max;
    send_data["ad_area_min"] = area_min;
    send_data["ad_area_max"] = area_max;
    send_data["bedrooms"] = bedrooms;
    send_data["bathrooms"] = bathrooms;
    send_data["cities"] = cities;
    send_data["air_conditioning"] = air_conditioning;
    send_data["parking"] = parking;
    send_data['sewer'] = sewer;
    send_data['water'] = water;
    send_data['microwave'] = microwave;
    send_data['swimming_pool'] = swimming_pool;
    send_data['barbecue'] = barbecue;
    send_data['lawn'] = lawn;
    send_data['tv_cable'] = tv_cable;
    send_data['wi_fi'] = wi_fi;
    send_data['gym'] = gym;
    send_data['church'] = church;
    send_data['mosque'] = mosque;
    send_data['school'] = school;
    send_data['market'] = market;
    send_data['hospital'] = hospital;
    send_data['resturant'] = resturant;
    send_data['beach'] = beach;
}

/**.
    Utility function to showcase the api data
    we got from backend to the table content
**/


function getAPIData() {
    $.ajax({
        method: 'GET',
        url: $(this).attr('action'),
        data: send_data,
        beforeSend: function(){
            $("#no_results h5").html("Loading data...");
        },
        success: function (result) {
            // putTableData(result);
        },
        error: function (response) {
            $("#no_results h5").html("Something went wrong");
            $("#list_data").hide();
            console.log(response)
        }
    });
}
