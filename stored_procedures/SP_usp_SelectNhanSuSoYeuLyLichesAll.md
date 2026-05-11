# Stored Procedure: `usp_SelectNhanSuSoYeuLyLichesAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.840000
- **Ngày sửa cuối**: 2014-10-14 10:39:41.153000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuSoYeuLyLichesAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuSoYeuLyLichesAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuSoYeuLyLichID],
	[MaNhanSu],
	[ThongTinCaNhanREF],
	[MaSoThue],
	[NgayBatDauLamViec],
	[NgayNghiViec],
	[ImageFileName],
	[ImageFIleNameEncode],
	[BiDanh],
	[NoiSinh],
	[NguyenQuan],
	[HoKhauThuongTru],
	[NoiOHienNay],
	[DanToc],
	[TonGiao],
	[TrinhDoVanHoa],
	[NgoaiNgu],
	[QuaTrinhBanThan],
	[CvFileName],
	[CvFIleNameEncode],
	[Code],
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
	[dbo].[NhanSuSoYeuLyLich]
Where DeletedStatus <> 1
--endregion


```
