# Stored Procedure: `ThucChay_InsertHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 10:19:08.680000
- **Ngày sửa cuối**: 2014-10-14 10:39:53.833000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_InsertHopDongChiTiet] 
	-- Add the parameters for the stored procedure here

AS
BEGIN

	delete from HopDongChiTietAllTemp
	
	INSERT INTO HopDongChiTietAllTemp	 					
							SELECT B.NgayDanhSoHopDong AS NgayThayDoi,	A.* 
							FROM dbo.HopDongChiTiet A
							INNER JOIN dbo.HopDong B ON A.HopDongFK = B.HopDongID
							WHERE A.DeletedStatus <> 1 AND B.DeletedStatus <> 1


	INSERT INTO HopDongChiTietAllTemp	
							SELECT *
							FROM  dbo.GetDistinctHopDongChiTietThayDoi()
END

```
