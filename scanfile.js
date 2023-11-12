export const scanTable = async (tableName) => {
    const params = {
        TableName: tableName,
    };

    const scanResults = [];
    let items;
    do{
        items = await documentClient.scan(params).promise();
        items.Items.forEach((item) => scanResults.push(item));
        params.ExclusiveStartKey = items.LastEvaluatedKey;
    }while(typeof items.LastEvaluatedKey !== "undefined");
    
    return scanResults;
};