# Stored Procedure: `prc_QLTC_GetDotChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-10-24 17:46:20.110000
- **Ngày sửa cuối**: 2025-04-11 10:03:58.860000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietREF` | `int(4)` | No |
| `@SkipCount` | `int(4)` | No |
| `@MaxResultCount` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_QLTC_GetDotChayHopDongChiTiet]
    -- Add the parameters for the stored procedure here
    @HopDongChiTietREF INT = 0,
    @SkipCount INT = 0,
    @MaxResultCount INT = 15
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Insert statements for procedure here
	WITH tblData AS (
	SELECT *
    FROM dbo.DotChayHopDongChiTiet
    WHERE HopDongChiTietREF = @HopDongChiTietREF
	)

	SELECT tbldt.*, totaldt.TotalRow FROM tblData tbldt
    CROSS JOIN (
		SELECT COUNT(1) AS TotalRow
		FROM tblData
	) totaldt
    ORDER BY CreatedAt DESC OFFSET @SkipCount ROWS FETCH NEXT @MaxResultCount ROWS ONLY;

    SELECT 
           'bookingREF',
           'thoiGianBatDau',
           'thoiGianKetThuc',
           'deletedStatus',
           'createdAt',
           'lastModifiedAt',
		   'dotChayHopDongChiTietID',
           'viTri',
           'tenWebsite',
           'hopDongREF',
           'hopDongChiTietREF',
           'thoiGianBatDauBooking',
           'thoiGianKetThucBooking',
           'ghiChu',
           'isWarning',
           'dmBannerREF',
           'tenBanner',
           'createdBy',
           'lastModifiedBy',
           'printStatus',
           'recordStatus';

END;









```
