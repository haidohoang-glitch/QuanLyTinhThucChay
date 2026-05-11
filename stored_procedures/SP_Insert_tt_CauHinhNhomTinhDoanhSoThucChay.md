# Stored Procedure: `Insert_tt_CauHinhNhomTinhDoanhSoThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-12-29 15:28:46.130000
- **Ngày sửa cuối**: 2022-01-24 16:30:46.047000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@NhomTinhDoanhSoThucChay` | `int(4)` | No |
| `@ThongTinJobChay` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[Insert_tt_CauHinhNhomTinhDoanhSoThucChay]
	@DmSanPhamREF = 5205,
	@NhomTinhDoanhSoThucChay = 1, --1: NHOM TINH SAN PHAM THUCCHAY THEO CHI PHI
	@ThongTinJobChay = N'ThucChay_TinhChiPhiKhac_ByJobs -> sp_TC_InsertThucChayDaTinh_ChiPhiKhac'
*/
CREATE PROCEDURE [dbo].[Insert_tt_CauHinhNhomTinhDoanhSoThucChay]
	@DmSanPhamREF INT,
	@NhomTinhDoanhSoThucChay INT, --1: NHOM TINH SAN PHAM THUCCHAY THEO CHI PHI
	@ThongTinJobChay NVARCHAR(200)
AS
    BEGIN
		IF(NOT EXISTS(SELECT TOP (1) DmSanPhamREF 
					FROM [dbo].[CauHinhNhomTinhDoanhSoThucChay] 
					WHERE DmSanPhamREF = @DmSanPhamREF
					AND [DeletedStatus] = 0 
		))
		BEGIN
			INSERT INTO [dbo].[CauHinhNhomTinhDoanhSoThucChay]
				   ([DmSanPhamREF]
				   ,[TenSanPham]
				   ,[NhomTinhDoanhSoThucChay]
				   ,[ThongtinJobChay]
				   ,[DeletedStatus]
				   ,[RecordStatus]
				   ,[CreatedAt]
				   ,[CreatedBy]
				   ,[LastModifiedAt]
				   ,[LastModifiedBy])
		SELECT TOP 1 sp.DmSanPhamID AS [DmSanPhamREF],
					sp.TenSanPham AS [TenSanPham],
					@NhomTinhDoanhSoThucChay AS [NhomTinhDoanhSoThucChay],
					@ThongTinJobChay AS [ThongtinJobChay],
					0 AS [DeletedStatus],
					0 AS [RecordStatus],
					GETDATE() AS [CreatedAt],
					N'sp' AS [CreatedBy],
					GETDATE() AS [LastModifiedAt],
					N'sp' AS [LastModifiedBy]
		FROM dbo.DmSanPham sp
		WHERE sp.DmSanPhamID = @DmSanPhamREF
		ORDER BY sp.DmSanPhamID 
		END
		ELSE
		BEGIN
			PRINT N'San pham id:' + Convert(nvarchar(100),@DmSanPhamREF) + N' da ton tai trong table [CauHinhNhomTinhDoanhSoThucChay]'
		END
		
    END



```
