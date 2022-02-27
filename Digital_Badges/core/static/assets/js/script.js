$(document).ready(function () {    
    $('.close-icon, .edit-popup-bg, .view-popup-bg, .cancel-btn').click(function () {
        $('.edit-popup').css('display', 'none');
        $('.view-popup').css('display', 'none');
    });
})

file.onchange = evt => {
    const [img_file] = file.files;
    if (img_file) {
      img.src = URL.createObjectURL(img_file);
    }
    var txt = "";
    if (img_file) {
        if (file.files.length == 1) {
            for (var i = 0; i < file.files.length; i++) {
                var f = file.files[i];
                if ('name' in f) {
                    txt += f.name;
                }
            }
        }
    } else {
        if (file.value == "") {
            txt += "Select one or more files.";
        } else {
            txt += "The files property is not supported by your browser!";
            txt += "<br>The path of the selected file: " + file.value;
        }
    }
    document.getElementById("fileDetails").innerHTML = txt;
    
}

function update_badge(value){
    get_badge(value)
    $('.edit-popup').css('display', 'block');
}

function get_badge(i){
    $.ajax({
        url: "/ListofBadges/getbadge/"+i,
        type: 'GET',
        success: function (response) {
            response.data.forEach((map_element) => {
                document.getElementById("badge_id").value=map_element.id;
                document.getElementById("Name").value=map_element.Name;
                document.getElementById("Description").value=map_element.Description;
                document.getElementById("students").value=map_element.students;
                document.getElementById("img").src=map_element.Image_url;
            });
        },
        error: function (response) {
            console.log(response.errors)
        }
    });
}

function view_badge(value){
    get_badge_for_view(value)
    $('.view-popup').css('display', 'block');
}

function get_badge_for_view(i){
    $.ajax({
        url: "/ListofBadges/getbadge/"+i,
        type: 'GET',
        success: function (response) {
            response.data.forEach((map_element) => {
                var details="";
                details+="<h5 class='topic'>Badge Details</h5>";
                details+="<p>Badge Name: "+map_element.Name+"</p>";
                details+="<p>Badge Description: "+map_element.Description+"</p>";
                details+="<p>Eligible Students: "+map_element.students+"</p>";
                details+="<p>Badge Image: <img src="+map_element.Image_url+" class='img-responsive' style='width: 150px;height:150px'></p>";
                document.getElementById('badge_details').innerHTML=details;
            });
        },
        error: function (response) {
            console.log(response.errors)
        }
    });
}