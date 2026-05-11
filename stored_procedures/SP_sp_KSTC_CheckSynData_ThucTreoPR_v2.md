# Stored Procedure: `sp_KSTC_CheckSynData_ThucTreoPR_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-10-29 14:02:22.843000
- **Ngày sửa cuối**: 2021-12-30 13:52:18.760000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_CheckSynData_ThucTreoPR_v2]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
--select * from [asdag2].ThucTreo.dbo.ThucTreo_PR tt where tt.Id= 135079
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
-------------------------------------------2.1 Thực treo PR - năm 2019-------------------------------------------------------------------
    -- Insert statements for procedure here
	--select *  from [asdag2].ThucTreo.dbo.ThucTreo_PR where id= 502210
SELECT N'Đăng tin' as CheckSynData, '<=2019'[Nam], A.*,B.*,(A.DonGia- B.GiaTien)LechGia, (A.ChietKhau - B.ChietKhau)LechChietKhau--,
--(case when A.Deleted_Status <> B.DeletedStatus then 'True' else 'False' end  ) TrangThaiXoa
FROM (
SELECT Contract_Id, Contract_Detail_Id, Product_Id,tt.Id,DonGia,ChietKhau,ThanhTien,tt.Deleted_Status,tt.Created_At,tt.Last_Modified_At
FROM [asdag2].ThucTreo.dbo.ThucTreo_PR tt
left join [asdag2].CONTRACT.dbo.CONTRACTS hd on tt.Contract_Id = hd.ID
WHERE 1=1 
--AND tt.Id=666
 --AND tt.Deleted_Status =0 
 AND isnull(tt.Created_At,'1900-01-01') < convert(date,getdate())
 and tt.Last_Modified_At >='2020-01-01'
 AND hd.[CONTRACT_YEAR]<=2019

)A
FULL OUTER JOIN
--LEFT JOIN
(
SELECT hd.SoHopDong, HopDongREF,HopDongChiTietREF,DmSanPhamREF, DmNhanHangREF, ThucChayHopDongChiTietPRID IDtt, GiaTien,ChietKhau,ttr.DeletedStatus,ttr.CreatedAt,ttr.LastModifiedAt 
FROM dbo.ThucChayHopDongChiTietPR ttr 
left join HopDong hd on HopDongREF = HopDongID
WHERE 1=1
--AND ttr.ThucChayHopDongChiTietPRID =502210
AND ttr.CreatedAt < convert(date,getdate())
and ttr.LastModifiedAt >='2020-01-01'
--AND ttr.DeletedStatus = 0 
AND hd.Nam <=2019
--AND ThanhTien <> 0
--and ttr.ThucChayHopDongChiTietPRID not in (select Idtt from idtt)
)B
ON A.Id = B.IDtt
WHERE A.Id IS NULL OR B.IDtt IS NULL
OR A.DonGia <> B.GiaTien 
OR A.Deleted_Status <> B.DeletedStatus
OR A.ChietKhau <> B.ChietKhau
ORDER BY A.Last_Modified_At,B.LastModifiedAt DESC


-------------------------------------------2.2 Thực treo PR - năm 2020-------------------------------------------------------------------
SELECT N'Đăng tin' as CheckSynData, '>=2020'[Nam],A.*,B.*,(A.DonGia- B.GiaTien)LechDonGia, (A.ChietKhau - B.ChietKhau)LechChietKhau, 
--(case when A.Deleted_Status <> B.DeletedStatus then 'True' else 'False' end  ) TrangThaiXoa,
(case when A.Contract_Detail_Id <> B.HopDongChiTietREF then 'True' else 'False' end  ) LechPhanBoID
FROM (
SELECT Contract_Id, Contract_Detail_Id, Product_Id,Id,DonGia,ChietKhau,ThanhTien,Deleted_Status,Created_At,Last_Modified_At
FROM [asdag2].ThucTreo.dbo.ThucTreo_PR tt
WHERE 1=1 and RIGHT(contract_number,2) >='20'
--AND Id=8214
 --AND Deleted_Status =0
 AND isnull(Created_At,'1900-01-01') <convert(date,getdate())
 --and tt.Contract_Id=1027760

)A
FULL OUTER JOIN
--LEFT JOIN
(
SELECT HopDongREF,HopDongChiTietREF,DmSanPhamREF, ThucChayHopDongChiTietPRID IDtt, GiaTien,ChietKhau,ttr.DeletedStatus,ttr.CreatedAt,ttr.LastModifiedAt 
FROM dbo.ThucChayHopDongChiTietPR ttr left join HopDong hd on HopDongREF = HopDongID
WHERE 1=1
AND ttr.CreatedAt <convert(date,getdate())
--AND ttr.DeletedStatus = 0 
--and ttr.HopDongREF= 1027760
AND  Nam >=2020
)B
ON A.Id = B.IDtt
WHERE A.Id IS NULL OR B.IDtt IS NULL
OR A.DonGia <> B.GiaTien 
OR A.Contract_Detail_Id <> B.HopDongChiTietREF
OR A.ChietKhau <> B.ChietKhau
or A.Deleted_Status <> B.DeletedStatus
ORDER BY A.Last_Modified_At,B.LastModifiedAt DESC
END

```
