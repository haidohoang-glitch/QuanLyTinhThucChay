# Stored Procedure: `usp_SelectHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:11:25.410000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.957000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectHopDong]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectHopDong]
	@HopDongID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[HopDongID],
	[DmMaHopDongREF],
	[TenMaHopDong],
	[So],
	[Thang],
	[Nam],
	[NgayKyHopDong],
	[NhanHopDong],
	[GiaTriHopDong],
	[SoHopDong],
	[NgayChuyenHopDongChoKeToan],
	[GhiChu],
	[NgayNhanHopDongBanCung],
	[DmKhachHangREF],
	[TenKhachHang],
	[SysNhanVienREF],
	[TenDangNhap],
	[TenNhanVien],
	[NgayDanhSoHopDong],
	[NganhHang],
	[DmNhomREF],
	[TrangThaiHopDong],
	[IsBanCung],
	[CongNo],
	[GhiChuHopDong],
	[NgayNhanBanFax],
	[LyDoHuyHopDong],
	[DangSuDung],
	[IsGiayPhep],
	[DmPhongBanREF],
	[TenPhongBan],
	[DmBoPhanREF],
	[TenBoPhan],
	[DmNhomLamViecREF],
	[TenNhom],
	[DmDiaDiemLamViecREF],
	[TenDiaDiemLamViec],
	[ChuyenTrang],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[HopDong]
WHERE
		[HopDongID] = @HopDongID
 and DeletedStatus <> 1

```
