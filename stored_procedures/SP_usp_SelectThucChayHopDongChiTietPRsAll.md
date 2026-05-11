# Stored Procedure: `usp_SelectThucChayHopDongChiTietPRsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-09 11:13:12.087000
- **Ngày sửa cuối**: 2014-11-19 12:24:44.983000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   ceo
-- Stored Procedure Name: [dbo].[usp_SelectThucChayHopDongChiTietPRsAll]
-- Create Date: 09 Tháng Bảy 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectThucChayHopDongChiTietPRsAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[ThucChayHopDongChiTietPRID],
	[HopDongREF],
	[HopDongChiTietREF],
	[NhanHang],
	[TenWebsite],
	[ChuyenMuc],
	[TieuDiem],
	[KhuyenMai],
	[GiaTien],
	[ThoiGianBatDau],
	[Link],
	[GhiChu],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[ThucChayHopDongChiTietPR]
Where DeletedStatus <> 1
--endregion

```
