# Stored Procedure: `sp_TC_CheckHopDongXoaPhanBo_DonViBai_Admatic_ThucTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-23 11:53:21.990000
- **Ngày sửa cuối**: 2021-06-23 11:53:36.090000

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
EXEC [sp_TC_CheckHopDongXoaPhanBo_DonViBai_Admatic_ThucTreo] '2018-06-13','2018-08-20','QC5620518',527807,'2018-08-29'
*/

CREATE  PROCEDURE [dbo].[sp_TC_CheckHopDongXoaPhanBo_DonViBai_Admatic_ThucTreo]
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

				EXEC [dbo].ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_DonViBai_Admatic 
				@NgayThucHien = @pNgayThucHien,
				@NgayGhiNhanThucChay = @pNgayThucHien,
				@HopDongID = @pHopDongID,
				@HopDongChiTietREF = @pHopDongChiTietID,
				@DmSanPhamREF = @pDmSanPhamREF,
				@GhiChu = @GhiChu
				IF(EXISTS(SELECT tcdt.HopDongChiTietREF FROM dbo.ThucChayDaTinh tcdt
					WHERE tcdt.HopDongID = @pHopDongID
					AND tcdt.HopDongChiTietREF = @pHopDongChiTietID
					AND tcdt.NgayThucHien <= @pNgayThucHien
					GROUP BY tcdt.HopDongChiTietREF HAVING SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) = 0
					AND SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) = 0)
				)
				BEGIN
					PRINT 'PHAN BO BI XOA'	
					UPDATE tt
					SET tt.RecordStatus = 0
					FROM dbo.ThucChayHopDongChiTiet tt
					WHERE 1=1 AND tt.HopDongREF = @pHopDongID
					AND tt.HopDongChiTietREF = @pHopDongChiTietID
				END
			END

    END




```
