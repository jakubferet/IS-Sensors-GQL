async function queryFetch(query){
    const response = await fetch('http://127.0.0.1:8000/gql/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
        body: JSON.stringify({
            query: query
        })
    });
    return await response.json();
}

function categoriesQuery(){
    const categories_collapse = document.getElementById('categories-collapse');
    queryFetch(
        `query{
            categories{
                id,name
            }
        }`
    ).then(data => {
        data.data.categories.forEach(category => {
            const list = createList(category);
            categories_collapse.append(list);
        }),
        console.log(data);
    });
}

function manufacturersQuery(){
    const manufacturers_collapse = document.getElementById('manufacturers-collapse');
    queryFetch(
        `query{
            manufacturers{
                id,name
            }
        }`
    ).then(data => {
        data.data.manufacturers.forEach(manufacturer => {
            const list = createList(manufacturer);
            manufacturers_collapse.append(list);
        }),
        console.log(data);
    });
}

function sensorsQuery(){
    const sensors_collapse = document.getElementById('sensors-collapse');
    queryFetch(
        `query{
            sensors{
                id,name
            }
        }`
    ).then(data => {
        data.data.sensors.forEach(sensor => {
            const list = createList(sensor);
            sensors_collapse.append(list);
        }),
        console.log(data);
    });
}

function createList(item){
    const a = document.createElement('a');
    a.setAttribute('class', 'list-group-item');
    a.setAttribute('href', '#');
    a.id = item.id;
    a.innerText = item.name;
    return a;
}

categoriesQuery()
manufacturersQuery()
sensorsQuery()