'本文档存储sql语句'
/*以下为联合tourist与notegeodate表的语句*/
select note.uid as uid, note.nid as nid,note.lat as noteLat, note.lng as noteLng, note.spot as spot, tourist.lat as touristLat, tourist.lng as touristLng, tourist.residence as residence, note.travelDate as travelDate
into outfile 'e:/experiment/travelDate.txt'
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
from notegeodata as note, tourist as tourist
where note.travelDate != '0000-00-00' and note.uid = tourist.uid and tourist.lat!=0

/*以下为统计tourist表中，游客居住地数目，与居住地游客数目的语句*/
SELECT  `residence` , COUNT( residence ) AS number
FROM  `tourist` 
GROUP BY residence
ORDER BY number DESC 
/*以下代码统计notegeodate中，travelDate与noteDate不在同一季度的日志不在同一季度的*/
select nid,travelSeason-noteSeason as diffSeason from(
select nid, quarter(`travelDate`) as travelSeason, quarter(DATE_SUB(`noteDate` INTERVAL 30 DAY) as noteSeason from(
	SELECT * FROM `notegeodata` where `travelDate`!= '0000-00-00'
	) as T1
) as T2
where travelSeason-noteSeason!=0;

/*以下代码统计tourist中，每个游客所发日志数与该游客的居住地经纬度信息*/
SELECT travelNote.uid as uid, count(travelNote.uid) as numberNotes, tourist.lat as ulat, tourist.lng as ulng
into outfile 'D:/touristInfo.txt'
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
FROM travelnote as travelNote, tourist
where travelNote.uid = tourist.uid and tourist.lng != 0
group by travelNote.uid
order by numberNotes desc

-- select notes with traveldate from table travelnote
SELECT * FROM `travelnote`
WHERE `travelDate`!='0000-00-00'
into outfile './notewithdate.txt'
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'