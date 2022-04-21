function calcualteDaysbetweenDates(date1, date2) {
  // The number of milliseconds in one day
  var ONE_DAY = 1000 * 60 * 60 * 24

  // Convert both dates to milliseconds
  var date1_ms = date1.getTime()
  var date2_ms = date2.getTime()

  // Calculate the difference in milliseconds
  var difference_ms = Math.abs(date1_ms - date2_ms)

  // Convert back to days and return
  return Math.round(difference_ms/ONE_DAY)
}

function calculateEuclideanDistance(point1, point2) {
  var x1 = point1.x
  var y1 = point1.y
  var x2 = point2.x
  var y2 = point2.y

    return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2))

    }


// get the data from the server
function getData(url, callback) {
    var xhr = new XMLHttpRequest()
    xhr.open('GET', url, true)
    xhr.onload = function() {
        if (xhr.status === 200) {
        callback(JSON.parse(xhr.responseText))
        }
    }
    xhr.send()
    }       

// publish a web page
function publish(url, data) {       
    var xhr = new XMLHttpRequest()
    xhr.open('POST', url, true)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(JSON.stringify(data))
    }

// get the RMSD of two coordinates arrays of different length
function getRMSD(coords1, coords2) {
    var sum = 0
    for (var i = 0; i < coords1.length; i++) {
        var diff = coords1[i] - coords2[i]
        sum += diff * diff
    }
    return Math.sqrt(sum / coords1.length)
    }   

// get RMSD between two pdb files  
function getRMSDfromPDB(pdb1, pdb2) {
    var coords1 = []
    var coords2 = []
    for (var i = 0; i < pdb1.length; i++) {
        if (pdb1[i].atom_name === 'CA') {
            coords1.push(pdb1[i].x)
            coords1.push(pdb1[i].y)
            coords1.push(pdb1[i].z)
        }
    }
    for (var i = 0; i < pdb2.length; i++) {
        if (pdb2[i].atom_name === 'CA') {
            coords2.push(pdb2[i].x)
            coords2.push(pdb2[i].y)
            coords2.push(pdb2[i].z)
        }
    }
    return getRMSD(coords1, coords2)
    }   
    // get RMSD between several pdb files
function getRMSDfromPDBArray(pdbArray) {
    var rmsd = 0
    for (var i = 0; i < pdbArray.length; i++) {
        for (var j = 0; j < pdbArray.length; j++) {
            if (i !== j) {
                rmsd += getRMSDfromPDB(pdbArray[i], pdbArray[j])
            }
        }
    }
    return rmsd / (pdbArray.length * (pdbArray.length - 1))
    }   
