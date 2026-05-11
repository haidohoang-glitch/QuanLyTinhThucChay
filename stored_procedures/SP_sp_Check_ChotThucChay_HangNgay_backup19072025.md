# Stored Procedure: `sp_Check_ChotThucChay_HangNgay_backup19072025`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-07-19 10:21:50.977000
- **Ngày sửa cuối**: 2025-07-19 10:21:50.977000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE  [dbo].[sp_Check_ChotThucChay_HangNgay_backup19072025]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @NgayThucHien nvarchar(50)
	SET @NgayThucHien = (select convert(date,max(ACTUAL_RUN_DATE)) from [ASDAG2].contract.dbo.CONTRACT_INFO_DATE_RUNNING_REAL)
    -- Insert statements for procedure here
	SELECT @NgayThucHien [ThucChayChotDenNgay], TC.SoHopDong,TC.HopdongID,TC.HopDongChiTietID, TC.tc,
	TC.NgayThucHien,--B.ID, B.CONTRACT_ID, B.PRODUCT_ID,
	B.MONEY_REAL_RUNING,B.DATE_REAL_RUNING,B.Deleted_Status, (TC.tc-B.MONEY_REAL_RUNING) Lech
	FROM (
SELECT A.SoHopDong,A.HopDongID,A.HopDongChiTietID, round(SUM(A.tc),0)tc, MAX(A.NgayThucHien)NgayThucHien FROM (
SELECT SoHopDong,HopdongID, HopDongChiTietID, SUM(ThanhTienThucChay)tc, MAX(NgayThucHien)NgayThucHien
FROM KS_ThucChay_TCDT
WHERE 1=1 and ngaythuchien <=@NgayThucHien
AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
and HopdongchitietID not in (0, 45890,52942,52943,53039,50351,52567,44268,46921,46922,20240,48674,44004,42278,33453) -- các pbo này từ năm 2014 về trước, k check nữa
GROUP BY  SoHopDong,HopdongID,HopDongChiTietID
)A
  GROUP BY A.SoHopDOng, A.HopDOngChiTietID,A.HopdongID, A.HopDongChiTietID  
)TC

LEFT JOIN 
(SELECT ID,CONTRACT_ID, MONEY_REAL_RUNING, DATE_REAL_RUNING, ct.PRODUCT_ID, ct.Deleted_Status FROM [ASDAG2].contract.dbo.contract_details ct
where
1=1 and Id not in (52942,52943,53039) -- -- các pbo này từ năm 2014 về trước, k check nữa
AND NOT ((PRODUCT_FORMALITY_ID = 13) OR 
 (EXISTS (SELECT a.CONTRACT_DETAIL_ID 
   FROM [ASDAG2].CONTRACT.dbo.CONTRACT_DETAIL_PRODUCT_PROPERTIES a 
   WHERE a.PRODUCT_CONFIG_PROPERTY_ID = 5 
   AND a.VALUE = 18 
   AND a.DELETED_STATUS = 0 
   AND a.CONTRACT_DETAIL_ID = ct.ID)
 )
))B

ON TC.HopDongChiTietID =B.ID and TC.HopDongID = B.CONTRACT_ID

WHERE  abs(ISNULL(TC.tc,0) - ISNULL(B.MONEY_REAL_RUNING,0) ) >100
ORDER BY TC.NgayThucHien DESC
END

```
