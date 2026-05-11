# Stored Procedure: `TestOutput`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-31 11:43:39.190000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.650000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ID` | `int(4)` | No |
| `@HoVaTen` | `nvarchar(400)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[TestOutput]
	-- Add the parameters for the stored procedure here
	@ID INT,
	@HoVaTen NVARCHAR(200) OUTPUT
AS
BEGIN
	--SELECT @HoVaTen = HoVaTen
	--FROM        (SELECT       STUFF(      (      SELECT CAST(',' as VARCHAR(MAX)) +  'N''''' + U.HoVaTen+ ''''''      FROM (     SELECT DISTINCT      A.NhanSuSoYeuLyLichID, A.HoVaTen     FROM NhanSuSoYeuLyLichFull A      INNER JOIN NhanSuQuaTrinhCongTac B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF AND B.[Active] = 1     WHERE       B.DmChucDanhREF IN (8,9,10,26,27,28)      AND B.DmBophanREF = 53 OR A.NhanSuSoYeuLyLichID = 153) U      ORDER BY U.HoVaTen      FOR XML PATH('')       ), 1, 1, '') AS HoVaTen      ) AS T     
    --FROM NhanSuSoYeuLyLichFull  
    --WHERE NhanSuSoYeuLyLichID = @ID;
    
    SET @HoVaTen =  dbo.Fn_NhanSu_GetListNhanVienByChucDanh(153)
END

```
