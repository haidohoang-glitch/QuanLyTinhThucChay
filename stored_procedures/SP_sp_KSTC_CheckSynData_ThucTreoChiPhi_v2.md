# Stored Procedure: `sp_KSTC_CheckSynData_ThucTreoChiPhi_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-10-29 14:05:51.053000
- **Ngày sửa cuối**: 2021-12-30 13:55:19.530000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[sp_KSTC_CheckSynData_ThucTreoChiPhi_v2] 
	-- Add the parameters for the stored procedure here

AS
BEGIN
-------------------------------------------1. kiem tra syn thuc treo chi phi bản ghi được duyệt----------------------------
SELECT N'Chi phí' as CheckSynData, N'Content, Khác' [LoaiChiPhi], A.*,B.*,(A.TotalMoney- B.ThanhTien)LechTien,
(case when A.Contract_Detail_Id <>  B.HopDongChiTietREF then 'x' else '' end) LechHDCT,
(A.Quantity - B.SoLuongThucTreo)LechSL,
(case when A.Discount <> B.ChietKhau then 'x' else '' end ) LechCK,
(case when A.product_formality_id <> B.DmHinhThucQuangCaoREF then 'x' else '' end )LechHTQC,
(case when A.Brand_id <> B.DmNhanHangREF then 'x' else '' end )LechNhanHang,
(case when A.RecordStatus <> B.RecordStatus then  'x' else '' end) LechTrangThai

FROM (
--select distinct Contract_Id, Contract_Detail_Id,Brand_id, product_formality_id,Product_Id,Id, Quantity,Discount,TotalMoney,DeletedStatus,RecordStatus,CreatedAt, LastModifiedAt  from  (
SELECT Contract_Id, Contract_Detail_Id,Brand_id, product_formality_id,Product_Id,Id, Quantity,Discount,TotalMoney,CreatedAt, LastModifiedAt , RecordStatus
FROM [ASDAG2].ThucTreo.dbo.ThucTreo_ChiPhi tt
WHERE 1=1 --and tt.Id =8020
AND tt.ID NOT IN (115493,108132,100614,100469,100468,99698,97027,95170,93913,93907,112956,114316,114324,114334,114335,115104,117234,117338,117859,117860,117861,117862,117863,117855,119911,119912,504591)
 AND DeletedStatus =0
 AND RecordStatus in (1,2,3)
 AND CreatedAt < convert(date,getdate())
 and LastModifiedAt >='2020-01-01'
 --and tt.Product_id not in (735,598,240,342,140,549) -- chi phi sản phẩm chính không check ở đây
 --and tt.id = 517519
 union all

 SELECT   Contract_Id, Contract_Detail_Id,Dm_NhanHang_Id Brand_id, product_formality_id,Product_Id,Id, 1 Quantity,ChietKhau Discount,ThanhTien TotalMoney,Created_At CreatetAt, Last_Modified_At LastModifiedAt
 ,2 RecordStatus
FROM [ASDAG2].ThucTreo.dbo.ThucTreo tt
WHERE 1=1 --and tt.Id =44484
 AND Deleted_Status =0
 AND Created_At < convert(date,getdate())
  and Last_Modified_At >='2020-01-01'
 and tt.Id in (36621,51991,518979,518978,518977,88701,88702,88703,88704,88705,89592,89593,89594,89595,89596,89597,89598,89599,89600,89601,89602,89603,43100,45217,45221,29911,29929,85097,85172,516190,516183,516184,61550,63523,63524,44484,34599,34600,30312,38318,38320,32279,32824,32935,33023,33217,33737,34165,515594,515595,515596,515597,515598,515599,40684,508739,110910,110914,110915,110916,110917,110918,110919,110920,110921,110922,110923,110924,110925,110926,110927,110928,110929,110930,110931,110932,110933,110934,110935,110941,110942,110943,110944,110945,110946,110947,110948,110949,110950110951,110952,110953,
110954,110955,110956,110957,110958,110959,110960,110961,110962,114252,117707,86164,45869,52009,52010,52011,52012,52013,52014,53800,53801,5380445711,45712,45713,45715,45716,45717,45718,45719,45720,45721,45722,45723,45724,45725,45726,45727,45728,27944,28219,29705,32483,52420,45414,39388,38414,38978,39036,39466,39956,41581,41582,
42126,42128,42147,43229,43230,43231,43737,44157,44428,44429,45326,45677,45774,45775,45729,45730,45731,45732,45733,45734,45735,45736,45737,45738,45739,45740,45741,45742,45743,45744,45745,
45746,45747,45748,45749,45750,45751,45752,45753,45754,45755,45756,45757,45758,45759,45760,45761,45762,45763,45764,45765,45766,45767,45768,45769,45770,45771,45772,45773,45993,46207,46221,
46222,46223,46224,46225,46229,46230,46231,46232,46233,46234,46235,46236,46237,46238,46240,46241,46242,46243,46245,46246,46247,46248,46249,46250,46251,46252,46253,46254,46268,51613,62187,
62188,62189,62190,62191,62192,62193,62194,62173,621773652,73653,73654,73655,73656,73657,73658,73659,73660,73661,83429,83256,83257,83258,83259,83260,83261,83262,83263,86279,86280,86281,86282,86283,
86284,86285,86286,86287,86288,86289,86290,86291,86292,86293,86294,86295,86296,86297,86298,86299,86300,86301,86302,86303,86304,86305,86306,86307,86308,86309,86310,86311,86312,86313,86314,86315,86316,86317,86771,86772,86773,86868,92583,62819,
62839,62840,62841,62842,62843,62844,62845,62846,64285,70883,70924,70926,70928,70929,70930,49750,49880,49881,51291,51292,51294,51992,52172,52246,52249,52250,52251,52807,52831,56653,62164,62165,62166,
62167,62168,62169,62170,62171,62172,62159,62160,62161,62162,62163,62195,62196,62492,62814,62816,62817,62818,63525,68567,68569,68570,68571,68572,68573,68575,68576,68577,68578,86785,86786,86787,86788
,45711,62174,73652,53804
)--thuctreo
)A
FULL OUTER JOIN
(
SELECT HopDongREF,HopDongChiTietREF,DmNhanHangREF,DmHinhThucQuangCaoREF,DmSanPhamREF, ThucChayHopDongChiTietID IDtt,SoLuongThucTreo,ChietKhau, ThanhTien,DeletedStatus,CreatedAt,LastModifiedAt 
, 2 RecordStatus
FROM dbo.ThucChayHopDongChiTiet ttr
WHERE 1=1 --and ttr.ThucChayHopDongChiTietID=45712
--AND DmSanPhamREF NOT IN (141,140,585,549,240,339,370,342,613,144,375,628,598,228,381,241,228,385,733,735,564,720,722,680,637,305,5133)	
AND LoaiThucTreo ='ChiPhi'
 AND CreatedAt < convert(date,getdate())
 and LastModifiedAt >='2020-01-01'
AND DeletedStatus = 0 
and HopDongChiTietREF <> 0
AND ttr.ThucChayHopDongChiTietID NOT IN (115493,108132,100614,100469,100468,99698,97027,95170,93913,93907,112956,114316,114324,114334,114335,115104,117234,117338,117859,117860,117861,117862,117863,117855,119911,119912,504591,8020,7923
,110950,110951
)

)B
ON A.Id = B.IDtt
WHERE (A.Id IS NULL OR B.IDtt IS NULL
OR A.TotalMoney <> B.ThanhTien 
OR A.Contract_Detail_Id <> B.HopDongChiTietREF
OR A.Quantity <> B.SoLuongThucTreo 
OR A.Discount <> B.ChietKhau
OR A.product_formality_id <> B.DmHinhThucQuangCaoREF
OR A.Brand_id <> B.DmNhanHangREF
OR A.RecordStatus <> B.RecordStatus)
and not (A.RecordStatus in (1,3) and B.RecordStatus is null)
ORDER BY A.LastModifiedAt desc

-------------------------------------------2.2.2 kiem tra ban ghi bị xóa ------------------------------------------------------

SELECT  N'Chi phí' as CheckSynData, N'Content, Khác' [LoaiChiPhi],A.*,B.* FROM (
SELECT b.contract_number, Contract_Id, Contract_Detail_Id, Product_Id,a.Id, TotalMoney,a.DeletedStatus,a.RecordStatus,a.CreatedBy,a.CreatedAt,a.LastModifiedBy, a.LastModifiedAt 
FROM [ASDAG2].ThucTreo.dbo.ThucTreo_ChiPhi a LEFT JOIN [ASDAG2].CONTRACT.dbo.contracts b ON a.Contract_Id = b.Id
WHERE 1=1
AND a.Id NOT IN (515429,515361,515331,515256,515167,
515166,515168,512992,505953,505956,510939,510938,510940,510941,510916,509803,509802,506747,
508622,508286,508285,508230,508253,508263,508262,508261,508260,508259,508258,508257,508252,
508251,508249,508250,508248,508246,508245,508244,508243,508236,508235,508234,508202,503252,
508117,508052,507942,507777,507551,505248,507446,507358,506750,506361,506360,506362,506778,
507040,506761,506762,506763,506765,506735,506410,506045,505732,505731,504794,504722,503265,
503203,503151,502925,502717,501463,501430,500083,500077,500006,500002,500001,115493,99698,
515792,515791,515794,515793,515795,515796,515797,515686,515672,515671,515670,
515635,515610,515451)
AND a.DeletedStatus =1
)A
--FULL OUTER JOIN
LEFT JOIN
(
SELECT HopDongREF,HopDongChiTietREF,DmSanPhamREF, ThucChayHopDongChiTietID IDtt, ThanhTien,DeletedStatus,LastModifiedAt
FROM dbo.ThucChayHopDongChiTiet ttr
WHERE 1=1
AND DmSanPhamREF NOT IN (141,140,585,549,240,339,370,342,613,423,306,144,375,628,598,228,381,241,228,385,733,735,564,720,722,680,821,637,305,5133)	
AND ttr.ThucChayHopDongChiTietID NOT IN (115493,99698)
and ttr.HopDongChiTietREF <> 0
)B
ON A.Contract_Detail_Id= B.HopDongChiTietREF
AND A.Id = B.IDtt
WHERE (A.Id IS NULL OR B.IDtt IS NULL
OR A.DeletedStatus <> B.DeletedStatus )
and B.IDtt is not null
--OR a.LastModifiedAt <> B.LastModifiedAt
ORDER BY A.LastModifiedAt DESC
END

```
