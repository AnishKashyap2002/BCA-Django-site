
var followers = parseInt(document.getElementById('followers').value )
var following = parseInt(document.getElementById('following').value)
var posts = parseInt(document.getElementById('posts').value)
var notes = parseInt(document.getElementById('notes').value)
var polls = parseInt(document.getElementById('polls').value)
var rooms = parseInt(document.getElementById('rooms').value)
var questions = parseInt(document.getElementById('questions').value)

console.log([followers, following, posts])

console.log('Fuck')
new Chart("chart", {
    type: 'radar',
    data: {
      labels: ['Followers', 'Following', 'Posts', 'Notes', 'Polls', 'Rooms', 'Questions'],
      datasets: [
        {
          data: [followers, following, posts, notes, polls, rooms, questions],
          backgroundColor :' #aae6ee',
        
        
        },
      ],
    },
    options: {
      title: {
        display: false,
      },
      scales: {
        yAxes: [{
            ticks: {
                suggestedMin: 0
            }
        }]
    },
      responsive:true,
    },
  });