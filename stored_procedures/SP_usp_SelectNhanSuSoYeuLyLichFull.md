# Stored Procedure: `usp_SelectNhanSuSoYeuLyLichFull`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:30.200000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.500000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuSoYeuLyLichID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuSoYeuLyLichFull]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuSoYeuLyLichFull]
	@NhanSuSoYeuLyLichID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuSoYeuLyLichID],
	[MaNhanSu],
	[HoVaTen],
	[BiDanh],
	[NgaySinh],
	[NoiSinh],
	[GioiTinh],
	[SoCMT],
	[CapTai],
	[NgayCap],
	[NguyenQuan],
	[HoKhauThuongTru],
	[NoiOHienNay],
	[DanToc],
	[TonGiao],
	[TrinhDoVanHoa],
	[NgoaiNgu],
	[QuaTrinhBanThan],
	[BanMem],
	[GhiChu],
	[Email],
	[DienThoai],
	[DienThoai1],
	[DienThoai2],
	[Code],
	[NgayNghiViec],
	[NgayBatDauLamViec],
	[ImageFIleName],
	[ImageFIleNameEncode],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[NhanSuSoYeuLyLichFull]
WHERE
		[NhanSuSoYeuLyLichID] = @NhanSuSoYeuLyLichID
 and DeletedStatus <> 1

--endregion

```
