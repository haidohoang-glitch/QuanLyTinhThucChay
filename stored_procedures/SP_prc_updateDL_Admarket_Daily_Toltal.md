# Stored Procedure: `prc_updateDL_Admarket_Daily_Toltal`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-03-19 18:18:32.593000
- **Ngày sửa cuối**: 2025-07-16 11:49:25.843000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngaythuchien` | `date(3)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[prc_updateDL_Admarket_Daily_Toltal]
		@ngaythuchien DATE = null
AS
BEGIN
    SET NOCOUNT ON;
	----cập nhật danh mục vị trí, sản phẩm vào bảng dữ liệu Lấy từ API số tổng sản phẩm 
 IF @ngaythuchien IS NULL 
	SET @ngaythuchien = CONVERT(DATE,GETDATE())

 UPDATE  dbo.ThucChayAdmarket_Total SET DmSanPhamREF=(CASE WHEN tc.product IN (N'adx_pc',N'adx_mobile',N'adx_ecom',N'adx_leadform') THEN '585'
                              WHEN tc.product=N'cpc' THEN '144'
							  WHEN tc.product=N'mktf' THEN '817'
                              ELSE '999' End),
                    TenSanPham =(CASE WHEN tc.product IN (N'adx_pc',N'adx_mobile',N'adx_ecom',N'adx_leadform') THEN N'ADX'
                              WHEN tc.product= N'cpc' THEN N'CPC Admarket'
							  WHEN tc.product= N'mktf' THEN N'Marketing fee – Chi phí marketing'
                              ELSE '999' End),
                    TenViTri=(CASE WHEN TC.product=N'adx_pc' THEN N'ADX'
                            WHEN TC.product=N'adx_mobile' THEN N'AdX Mobile'
                            WHEN TC.product=N'adx_ecom' THEN N'AdX Ecommerce'
                            WHEN TC.product=N'adx_leadform' THEN N'Adx Leadform'
                            WHEN TC.product=N'cpc' THEN N'CPC Admarket'
							WHEN TC.product=N'mktf' THEN N'Null'
                            ELSE '999' END),
                    DmViTriREF=(CASE WHEN TC.product=N'adx_pc' THEN '1'
                            WHEN TC.product=N'adx_mobile' THEN '2'
                            WHEN TC.product=N'adx_ecom' THEN '3'
                            WHEN TC.product=N'adx_leadform' THEN '4'
							WHEN TC.product=N'mktf' THEN N'Null'
                            WHEN TC.product=N'cpc' THEN '0'
                            ELSE '999' END)


                                               
 FROM dbo.ThucChayAdmarket_Total tc
 WHERE NgayThucHien=@ngaythuchien
 END;

```
