console.log('Loading function');

exports.handler = async (event) => {
    // TODO implement
    console.log('value1 =', event.key1);
    console.log('value2 =', event.key2);
    console.log('value3 =', event.key3);
    return event.key1;
};