
console.log("Recommend");
fetch('https://reqres.in/api/users?page=2').then(response => response.json())
.then(responseJSON => RecommendsList(responseJSON.data)).catch(err => 
    console.log(err));

function RecommendsList(users){
    console.log(users);
    const curr_main = document.querySelector("main");
    for(let user of users){
        const selection = document.createElement("section");
        selection.innerHTML = `${user.first_name} ${user.last_name}
        <br><a href="mailto:${user.email}">Contact Email</a><br>
        <img src="${user.avatar}" alt="ProPic"/><br><br>` ;
        curr_main.appendChild(selection);
    }  
}