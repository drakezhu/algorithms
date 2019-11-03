val lines = spark.read.textFile( "gs://comp119/testFile.csv").rdd
val links = lines.map{ s => val parts = s.split("\\,"); (parts(0), parts(1), parts(2)) }.distinct().groupByKey().cache()
var ranks = links.mapValues(v => 1.0)
val iters = 5

for (i <- 1 to iters) { val contribs = links.join(ranks).values.flatMap{
 case (urls, rank) => val size = urls.size; urls.map(url => (url, rank / size)) };  

 ranks = contribs.reduceByKey(_ + _).mapValues(0.15 + 0.85 * _) }
ranks.collect().foreach(println)

