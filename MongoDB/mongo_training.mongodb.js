
// creating a collection
use('demo')
db.createCollection('myconnection')

// querying the database
use('demo')
db.inventory.insertMany([
    { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
    { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
    { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
    { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
    { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
 ]);

// $and query 
use('demo')
db.inventory.find({$and: [{status: "A"}, {qty: {$gt: 40}}]})

// query to embedded documents
use('demo')
db.inventory.find({size: { h: 14, w: 21, uom: "cm" }})

use('demo')
db.inventory.find({"size.h": 8.5})


use('sample_airbnb')

db.listingsAndReviews.find({$and: 
    [{ "host.host_response_rate": { $lte: 50 } }, 
    { bedrooms: 2 }]})


use('demo')
db.inventory2.insertMany([
    { item: "journal", qty: 25, tags: ["blank", "red"], dim_cm: [ 14, 21 ] },
    { item: "notebook", qty: 50, tags: ["red", "blank"], dim_cm: [ 14, 21 ] },
    { item: "paper", qty: 100, tags: ["red", "blank", "plain"], dim_cm: [ 14, 21 ] },
    { item: "planner", qty: 75, tags: ["blank", "red"], dim_cm: [ 22.85, 30 ] },
    { item: "postcard", qty: 45, tags: ["blue"], dim_cm: [ 10, 15.25 ] }
    ]);

// query to array of documents with order

use('demo')
db.inventory2.find({ tags: ["red", "blank"] })

// query to array of documents without order

use('demo')
db.inventory2.find({ tags: { $all: ["red", "blank"]} })

use('demo')
db.inventory2.find({ tags: { $all: ["red", "blank"], $size: 2 } })

// dim_cm array contains at least one element whose value is less than 15
use('demo')
db.inventory2.find( { "dim_cm.0" : { $gt: 15 } } )


// Query to replace a document
use('demo')
db.inventory2.replaceOne({ _id:ObjectId("6464d0d761f8afe4cf117cf5")},
                        {item:"journal2", qty:25, tags:["blank", "red"], dim_cm:[14,21]})


// Query to replace a document without upsert so it will not insert a new document as it is not present

use('demo')
db.inventory2.replaceOne({ _id:ObjectId("6464d0d761f8afe4cf117cf7")},
                        {item:"journal2", qty:25, tags:["blank", "red"], dim_cm:[14,21]})


// Query to upsert a new document using upsert:true
use('demo')
db.inventory2.replaceOne({ _id:ObjectId("6464d0d761f8afe4cf117cf7")},
                        {item:"journal2", qty:25, tags:["blank", "red"], dim_cm:[14,21]},
                        {upsert:true})



// Query to update a document

use('demo')
db.inventory.updateOne({ item: "paper" },
                        {$set: {"size.uom": "cm", status: "p"}})


use('demo')
db.inventory.updateMany({},
                        {$set: {"size.uom": "cm", status: "p"}})



// current date
use('demo')
db.inventory.updateOne({item: "paper"},
                        {$set: {qty:50},
                        $currentDate: {lastModified: true}})

use('demo')
db.inventory.find({item: "paper"})


// Delete document/s

use('demo')
db.inventory.deleteMany({ status : "A" } )

use('demo')
db.inventory.deleteOne( { status: "D" } )


// elemMatch
use('demo')
db.inventory.find({size: { $elemMatch: { "h": 14, "w": 21  } } } )