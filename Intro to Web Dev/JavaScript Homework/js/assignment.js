//Zachary Talarick
//I pledge my honor that I have abided by the stevens honor system. ztalaric
// Keep this for the students
var fileLocations = {
	woofer: 'assets/woofer.jpg',
	pupper: 'assets/pupper.jpg',
	clouds: 'assets/clouds.jpg',
	snek: 'assets/snek.jpg'
};

/**
 * This function will get the values of the following elements:
 * 		input-username, input-caption, input-picture
 * Then, this will pass those values to the addNewPost function.
 * 
 */
function handleFormSubmit() {
	// Get values of inputs
	// Pass values to addNewPost()
    var inputName = document.getElementById("input-username").value;
    var inputCaption = document.getElementById("input-caption").value;
    var inputPicture = document.getElementById("input-picture").value;
    addNewPost(inputName, inputPicture, inputCaption);
}

/**
 * This function create the following div and append it to the #post-list element
	<div class="post">
		<span>{username}</span>
		<img src="{img_src}" alt="{caption}">
		<div id="post-overlay">
			{caption}
		</div>
	</div>
 * 
 * Also, add a mouseover and mouseleave events to the post div for opacity 
 * transitions in the post-overlay div
 */
function addNewPost(username, img_src, caption) {
    var post = document.createElement("div");
    var image = document.createElement("img");
    var span = document.createElement("span");
    var overlay = document.createElement("div");
    
    overlay.id = "post-overlay";
    overlay.innerHTML = caption;
    overlay.style.transition = "all .5s";
    
    post.className = "post";
    span.innerHTML = username;

    image.src = "assets/" + img_src + ".jpg";
    post.appendChild(span);
    post.appendChild(image);
    post.appendChild(overlay);
    
    post.addEventListener("mouseover", function(event){
        event.target.style.opacity = "1";
        
    })
    post.addEventListener("mouseout", function(event){
        event.target.style.opacity = "0";
    })
    document.getElementById("post-list").appendChild(post);
}
