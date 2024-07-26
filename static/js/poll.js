$(document).ready(function () {
    choices = document.getElementsByClassName('choices')
    votes = document.getElementsByClassName('votes')

    let choice_list = [];
    let vote_list = [];
    for( let i = 0 ; i < choices.length; i++){
        choice_list.push(choices[i].value)
        vote_list.push(parseInt(votes[i].value))
    }
    console.log(choice_list, vote_list)

    new Chart("chart", {
        type: 'pie',
        data: {
          labels: choice_list,
          datasets: [
            {
              data: vote_list,
              backgroundColor :['rgba(255, 129, 102, 1)',
               'rgba(234, 162, 235, 1)',
               'rgba(255, 206, 36, 1)',
               'rgba(75, 192, 192, 1)',
               'rgba(153, 102, 255, 1)',
            ],
            
            borderColor: 'black',
            
            },
          ],
        },
        options: {
          title: {
            display: false,
            text: "This is For the Pie chart",
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

      $('#bar').click(function () {
        create_chart('bar')
        
      });
      $('#doughnut').click(function () {
        
        create_chart('doughnut')
        
      });

      $('#radar').click(function () {
        create_chart('radar')
        
      });
      function create_chart(type){
        new Chart("chart", {
          type: type,
          data: {
            labels: choice_list,
            datasets: [
              {
                data: vote_list,
                backgroundColor :['rgba(255, 129, 102, 1)',
                 'rgba(234, 162, 235, 1)',
                 'rgba(255, 206, 36, 1)',
                 'rgba(75, 192, 192, 1)',
                 'rgba(153, 102, 255, 1)',
              ],
              
              borderColor: 'black',
              
              },
            ],
          },
          options: {
            title: {
              display: false,
              text: "This is For the Pie chart",
            },
            scales: {
              yAxes: [{
                  ticks: {
                      suggestedMin: 0,
                  }
              }]
          },
          },
        });
      
      }

});



