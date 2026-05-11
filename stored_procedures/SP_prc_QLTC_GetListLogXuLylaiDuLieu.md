# Stored Procedure: `prc_QLTC_GetListLogXuLylaiDuLieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-07-05 15:56:56.677000
- **Ngày sửa cuối**: 2023-07-05 15:56:56.677000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(4000)` | No |
| `@BannerREF` | `nvarchar(4000)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@FromDate` | `datetime2(8)` | No |
| `@ToDate` | `datetime2(8)` | No |
| `@HopDongChiTiet` | `int(4)` | No |
| `@Type` | `int(4)` | No |
| `@Status` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[prc_QLTC_GetListLogXuLylaiDuLieu]
	-- Add the parameters for the stored procedure here
	@SoHopDong NVARCHAR(2000),
	@BannerREF NVARCHAR(2000),
	@DmSanPhamREF INT = 0,
	@FromDate DATETIME2(7),
	@ToDate DATETIME2(7),
	@HopDongChiTiet INT,
	@Type INT = 0,
	@Status INT = 0
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	IF(@Type = 1)
		BEGIN
			SELECT DISTINCT SoHopDong, Name_Table, HopDongChiTietREF, FromDate, ToDate, DmSanPhamREF 
			FROM [dbo].[DataLog_QLTC_XuLylaiDuLieu] 
			WHERE CAST(FromDate AS Date) = CAST(@FromDate AS Date)
			AND CAST(ToDate AS Date) = CAST(@ToDate AS Date)
			AND (ISNULL(@SoHopDong, '') = ''
					OR SoHopDong In (Select Name From STRING_SPLIT_QLTC(@SoHopDong)))
			AND (ISNULL(@HopDongChiTiet, 0) = 0
					OR HopDongChiTietREF = @HopDongChiTiet)
			AND (ISNULL(@BannerREF, '') = ''
					OR BannerREF In (Select Name From STRING_SPLIT_QLTC(@BannerREF)))
			AND (ISNULL(@DmSanPhamREF, 0) = 0
					OR DmSanPhamREF = @DmSanPhamREF)
			AND (ISNULL(@Status, 0) = 0
					OR [Status] = @Status)
		END
    ELSE
		BEGIN
			SELECT * FROM [dbo].[DataLog_QLTC_XuLylaiDuLieu] 
			WHERE CAST(FromDate AS Date) = CAST(@FromDate AS Date) 
			AND CAST(ToDate AS Date) = CAST(@ToDate AS Date)
			AND (ISNULL(@SoHopDong, '') = ''
					OR SoHopDong In (Select Name From STRING_SPLIT_QLTC(@SoHopDong)))
			AND (ISNULL(@BannerREF, '') = ''
					OR BannerREF In (Select Name From STRING_SPLIT_QLTC(@BannerREF)))
			AND (ISNULL(@DmSanPhamREF, 0) = 0
					OR DmSanPhamREF = @DmSanPhamREF)
			AND (ISNULL(@Status, 0) = 0
					OR [Status] = @Status)
		END
	
END

```
