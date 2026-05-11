# Stored Procedure: `API_GetByRequestKey_PerformanceBase_bk1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-16 16:34:53.110000
- **Ngày sửa cuối**: 2021-06-16 16:34:53.110000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@RequestKey` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql


-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
create PROCEDURE [dbo].[API_GetByRequestKey_PerformanceBase_bk1]
    -- Add the parameters for the stored procedure here
	@RequestKey NVARCHAR(500)
AS
BEGIN
    SET NOCOUNT ON;
    
	SELECT Id AS id,
           Request_key AS requestKey,
           SoHopDong AS soHopDong,
           HopDongID AS hopDongId,
           HopDongChiTietREF AS hopDongChiTietId,
           DmSanPhamREF AS sanPhamId,
           TenSanPham AS tenSanPham,
           TK_Admarket AS taiKhoan,
           ThanhTien AS thanhTien,
           DmViTriREF AS viTriId,
           TenViTri AS tenViTri,
           TienThucChayTong AS tienThucChayTong,
           TienThucChay AS tienThucChay,
           ThucChayDenNgay AS thucChayDenNgay,
           SoTienThayDoi AS soTienThayDoi,
           NgayGhiNhanThayDoi AS ngayGhiNhanThayDoi,
           CreatedAt AS createdAt,
           LastModifiedAt AS lastModifiedAt,
           CASE
				WHEN RecordStatus = 0 THEN N'Chưa ghi nhận'
				WHEN RecordStatus = 1 THEN N'Đã ghi nhận'
				WHEN RecordStatus = 2 THEN N'Từ chối'
				ELSE ''
			END AS trangThai
	FROM dbo.ThucChay_PerformanceBase_ThayDoi
	WHERE Request_key = @RequestKey
    
END;



```
