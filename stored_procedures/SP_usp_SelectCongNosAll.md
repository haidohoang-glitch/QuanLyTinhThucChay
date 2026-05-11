# Stored Procedure: `usp_SelectCongNosAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:02.220000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.223000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectCongNosAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectCongNosAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[CongNoID],
	[HopDongREF],
	[SoHoaDon],
	[NgayXuat],
	[GiaTri],
	[GiaTriThanhToan],
	[NgayThanhToan],
	[HanThanhToanID],
	[NgayTraHoaDon],
	[IsSoPhieuThu],
	[SoHoaDonGiamTru],
	[SoBangThongKe],
	[NgayChuyenChoKeToan],
	[Sign],
	[PhieuThuLinkNapTien],
	[TaiKhoanKhachHangREF],
	[GhiChu],
	[Active],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[CongNo]
Where DeletedStatus <> 1
--endregion

```
