function getArea(length, width) {
    let area;
    area = parseFloat(length * width)
    return area;
}

function getPerimeter(length, width) {
    let perimeter;
    perimeter = parseInt(2*(length+width))
    return perimeter;
}


function main() {
    const length = +(readLine());
    const width = +(readLine());
    
    console.log(getArea(length, width));
    console.log(getPerimeter(length, width));
}