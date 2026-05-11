# Stored Procedure: `Job_UpdateGiaTriThayDoi_ThucChayDaTinhAdmarket_NhanHangChuanHoa`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-09-26 14:17:21.193000
- **Ngày sửa cuối**: 2016-11-22 11:37:29.770000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Haidh
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[Job_UpdateGiaTriThayDoi_ThucChayDaTinhAdmarket_NhanHangChuanHoa]
CREATE PROCEDURE [dbo].[Job_UpdateGiaTriThayDoi_ThucChayDaTinhAdmarket_NhanHangChuanHoa]
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien =  DATEADD(DAY,-1, CONVERT(DATE,GETDATE()))

	EXEC [ThucChay_UpdateThucChayDaTinhAdmarket_NhanHangChuanHoa] @NgayThucHien,@NgayThucHien,0,@NgayThucHien
END



----CHECK DU LIEU
---EXEC [ThucChay_UpdateThucChayDaTinhAdmarket_NhanHangChuanHoa] '2016-09-25','2016-09-25',0,'2016-09-25'

--SELECT nh.DmNhanHangID, nh.TenNhanHang, nh.DmNhanHangThayDoiID
--		, nh.LastModidfiedBy, nh.LastModifiedAt 
--		FROM [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.DmNhanHang nh
--		WHERE ISNULL(nh.DmNhanHangThayDoiID,0) <> 0
--		AND nh.DeletedStatus = 1
--		AND CONVERT(DATE,nh.LastModifiedAt) = '2016-09-21'
```
