document.getElementById('submitButton').addEventListener('click',function() {
    var userhandle = document.getElementById('userhandle').value;
    var numberOfQuestions = document.getElementById('numberOfQuestions').value;
    var tags = document.getElementById('tags').value.split(',');


    // console.log(userhandle);
    // console.log(numberOfQuestions);
    // console.log(tags);
});

var data = {
    userhandle: userhandle,
    numberOfQuestions: numberOfQuestions,
    tags: tags
};

var jsonData = JSON.stringify(data);

fetch('Backend url',{
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => {
    var tableContainer = document.getElementById('tableContainer');

    var table = document.createElement('table');

    var thead = document.createElement('thead');
    var headerRow = document.createElement('tr');

    Object.keys(data[0]).forEach(key => {
        var th = ducument.createElement('th');
        th.textContent = key;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    var tbody = document.createElement('tbody');
    data.forEach(item => {
        var row = document.createElement('tr');
        Object.values(item).forEach(value => {
            var td = document.createElement('td');
            td.textContent = value;
            row.appendChild(td);
        });
        tbody.appendChild(row);
    });
    table.appendChild(tbody);
    tableContainer.appendChild(table);
})
.catch((error) => {
    console.error('Error: ',error);
});