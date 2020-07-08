const btnSubmit = document.querySelector('#submit');
const btnDelete = document.querySelector('#delete');
const text = document.querySelector('#input-text');
const textarea = document.querySelector('#output');
const chartEle = document.querySelector('#chart');

// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

function drawChart(title, data) {
    const dataTable = new google.visualization.DataTable();
    dataTable.addColumn('string', 'Type');
    dataTable.addColumn('number', 'Number');
    dataTable.addRows(data)

    const options = {
        title: title,
        width: screen.availWidth / 2,
        height: screen.availHeight / 2 - 10,
        backgroundColor: '#333333',
        legend: {
            textStyle: {
                color: 'white'
            }
        }
    }

    const chart = new google.visualization.PieChart(chartEle);
    chart.draw(dataTable, options)
}

function setDisable(state) {
    btnSubmit.disabled = state;
    btnSubmit.textContent = state ? "Loading..." : "Submit"
    btnDelete.disabled = state;
}

btnSubmit.addEventListener('click', async e => {
    e.preventDefault()

    setDisable(true);

    if (text.value === '') {
        alert("Xin vui lòng nhập dữ liệu!!!")
        setDisable(false);
        return;
    }

    const res = await fetch('/api/predict', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text.value })
    })

    const { title, probabilities } = await res.json();
    drawChart(title, Object.entries(probabilities));

    setDisable(false);
});

btnDelete.addEventListener('click', () => {
    chartEle.innerHTML = '';
    text.value = "";
})