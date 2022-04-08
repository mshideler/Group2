function test() {
    let changedElement = d3.select(this);
    // Save the value that was changed as a variable.
    let changedValue = changedElement.property('value');
    // Save the id of the filter that was changed as a variable.
    let filterID = changedElement.attr('id');
    console.log(changedValue);
  // Attach an event to listen for changes to each filter
}  
d3.selectAll('input').on('change',test);