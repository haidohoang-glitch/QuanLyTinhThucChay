# Stored Procedure: `sp_TC_CheckHopDongXoaPhanBo_DonViBai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-04 14:44:56.677000
- **Ngày sửa cuối**: 2021-03-05 15:59:04.413000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pHopDongID` | `int(4)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
| `@pDmSanPhamREF` | `int(4)` | No |
| `@pNgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


/*
EXEC [sp_TC_CheckHopDongXoaPhanBo_DonViBai] '2018-06-13','2018-08-20','QC5620518',527807,'2018-08-29'
*/

CREATE  PROCEDURE [dbo].[sp_TC_CheckHopDongXoaPhanBo_DonViBai]
   @pHopDongID INT
  , @pHopDongChiTietID INT
  , @pDmSanPhamREF INT
  , @pNgayThucHien DATETIME
AS
    BEGIN
		DECLARE @GhiChu NVARCHAR(1000) = ''
		IF(EXISTS(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet hdct
			WHERE hdct.DeletedStatus = 1 --phan bo bi xoa
			AND hdct.HopDongChiTietID = @pHopDongChiTietID
			AND hdct.HopDongFK = @pHopDongID
			AND hdct.DmSanPhamREF = @pDmSanPhamREF
			))
			BEGIN
				PRINT 'Thuc hien doi tru toan bo'
				SET @GhiChu = N'Doi tru phan bo bi xoa cho DonViBai HDCT:' + Convert(NVARCHAR(50),@pHopDongChiTietID)

				EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_CPM_DonViBai] 
				@NgayThucHien = @pNgayThucHien,
				@NgayGhiNhanThucChay = @pNgayThucHien,
				@HopDongID = @pHopDongID,
				@HopDongChiTietREF = @pHopDongChiTietID,
				@DmSanPhamREF = @pDmSanPhamREF,
				@GhiChu = @GhiChu
			END

    END




```
