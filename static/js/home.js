console.log('home connected')

const url = window.location.href
console.log('url', url)

const coursesNotEnrolledIn = document.getElementById("coursesNotEnrolledIn")

$.ajax({
	type: 'GET',
	url: `${url}course/course/data`,
	success: function(response) {
		console.log(response)
		let data = response.data
		
		console.log(data)
		data.forEach(el => {
			for (const [course] of Object.entries(el)) {
				coursesNotEnrolledIn.innerHTML += `
                    <hr>
                    <div class="">
                        <p>${course}</p>            
                    </div>
                    <br>
                `
                
			}
		});
	},
	error: function(error) {
        console.log(error)
    } 
})