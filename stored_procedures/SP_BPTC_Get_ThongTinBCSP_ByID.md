# Stored Procedure: `BPTC_Get_ThongTinBCSP_ByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.630000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ReportID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Get_ThongTinBCSP_ByID] ( @ReportID INT )
AS 
    BEGIN

        DECLARE @NamBaoCao INT
        SELECT  @NamBaoCao = YEAR(ThoiGianKetThuc)
        FROM    dbo.BPTC_BaoCaoTTSanPhamThang
        WHERE   BPTC_BaoCaoTTSanPhamThangID = @ReportID
    
        DECLARE @DonVi INT = 1000000000 --1 TỶ
        DECLARE @NhomSanPhamBaoCaoID INT
                
        SELECT  @NhomSanPhamBaoCaoID = NhomSanPhamBaoCaoID
        FROM    dbo.BPTC_BaoCaoTTSanPhamThang
        WHERE   BPTC_BaoCaoTTSanPhamThangID = @ReportID
	
	--1. THONG TIN CHUNG
        SELECT  BPTC_BaoCaoTTSanPhamThangID AS ReportID ,
                TenBaoCao ,
                NhomSanPhamBaoCaoID ,
                TenNhomSanPhamBaoCao,
                ThoiGianBatDau ,
                ThoiGianKetThuc ,
                NguoiLap ,
                NgayLap ,
                TrangThaiPheDuyet ,
                NguoiPheDuyet ,
                NgayPheDuyet ,
                CreatedBy ,
                CreatedAt ,
                LastModifiedBy ,
                LastModifiedAt
        FROM    dbo.BPTC_BaoCaoTTSanPhamThang
        WHERE   BPTC_BaoCaoTTSanPhamThangID = @ReportID
	
	--2. BPTC_BaoCaoTTSanPhamThang_DanhSo
        SELECT  ThoiGian ,
                CASE WHEN ThoiGian > 12 THEN N'Tổng'
                     ELSE 'T' + ThoiGian
                END AS ThoiGianShow ,
                ROUND(CONVERT(FLOAT, DoanhSoNamTruoc / @DonVi), 0) DoanhSoNamTruoc ,
                ROUND(CONVERT(FLOAT, ChiTieuHienTai / @DonVi), 0) ChiTieuHienTai ,
                ROUND(CONVERT(FLOAT, DoanhSoHienTai / @DonVi), 0) DoanhSoHienTai ,
                dbo.FormatNumber(DoanhSoNamTruoc) DoanhSoNamTruocShow ,
                dbo.FormatNumber(ChiTieuHienTai) ChiTieuHienTaiShow ,
                dbo.FormatNumber(DoanhSoHienTai) DoanhSoHienTaiShow ,
                ROUND(TiLeTTCungKy, 2) TiLeTTCungKy ,
                ROUND(TiLeHTChiTieu, 2) TiLeHTChiTieu ,
                ' ' AS ItemLabel
        FROM    BPTC_BaoCaoTTSanPhamThang_DanhSo
        WHERE   BPTC_BaoCaoTTSanPhamThangREF = @ReportID	
	
	--3. BPTC_BaoCaoTTSanPhamThang_ThucChay
        SELECT  ThoiGian ,
                CASE WHEN ThoiGian > 12 THEN N'Tổng'
                     ELSE 'T' + ThoiGian
                END AS ThoiGianShow ,
                ROUND(CONVERT(FLOAT, DoanhSoNamTruoc / @DonVi), 0) DoanhSoNamTruoc ,
                ROUND(CONVERT(FLOAT, ChiTieuHienTai / @DonVi), 0) ChiTieuHienTai ,
                ROUND(CONVERT(FLOAT, DoanhSoHienTai / @DonVi), 0) DoanhSoHienTai ,
                dbo.FormatNumber(DoanhSoNamTruoc) DoanhSoNamTruocShow ,
                dbo.FormatNumber(ChiTieuHienTai) ChiTieuHienTaiShow ,
                dbo.FormatNumber(DoanhSoHienTai) DoanhSoHienTaiShow ,
                ROUND(TiLeTTCungKy, 2) TiLeTTCungKy ,
                ROUND(TiLeHTChiTieu, 2) TiLeHTChiTieu ,
                ' ' AS ItemLabel
        FROM    BPTC_BaoCaoTTSanPhamThang_ThucChay
        WHERE   BPTC_BaoCaoTTSanPhamThangREF = @ReportID
	
	--4. BPTC_BaoCaoTTSanPhamThang_ThucChay_DanhSo
        SELECT  ThoiGian ,
                CASE WHEN ThoiGian > 12 THEN N'Tổng'
                     ELSE 'T' + ThoiGian
                END AS ThoiGianShow ,
                ROUND(CONVERT(FLOAT, DoanhSoDanhSo / @DonVi), 0) DoanhSoDanhSo ,
                ROUND(CONVERT(FLOAT, DoanhSoThucChay / @DonVi), 0) DoanhSoThucChay ,
                dbo.FormatNumber(DoanhSoDanhSo) DoanhSoDanhSoShow ,
                dbo.FormatNumber(DoanhSoThucChay) DoanhSoThucChayShow ,
                ROUND(TiLeThucChay_DanhSo, 2) TiLeThucChay_DanhSo ,
                ' ' AS ItemLabel
        FROM    BPTC_BaoCaoTTSanPhamThang_ThucChay_DanhSo
        WHERE   BPTC_BaoCaoTTSanPhamThangREF = @ReportID
	
	--5. COMMENTS
        CREATE TABLE #COMMENT
            (
              PageFooter NVARCHAR(255) ,
              PageHeader1 NVARCHAR(255) ,
              NguoiLap NVARCHAR(255) ,
              NgayBatDau DATETIME ,
              NgayKetThuc DATETIME ,
              NoiDungDanhGia_SanPham_DanhSo NVARCHAR(500) ,
              NoiDungDanhGia_SanPham_ThucChay NVARCHAR(500) ,
              NoiDungDanhGia_SanPham_ThucChay_DanhSo NVARCHAR(500)
            )
        
        DECLARE @PageFooter NVARCHAR(255)
        DECLARE @PageHeader1 NVARCHAR(255)
        DECLARE @NgayBatDau DATETIME
        DECLARE @NgayKetThuc DATETIME
        
        DECLARE @NoiDungDanhGia_SanPham_DanhSo NVARCHAR(500)
        DECLARE @NoiDungDanhGia_SanPham_ThucChay NVARCHAR(500)
        DECLARE @NoiDungDanhGia_SanPham_ThucChay_DanhSo NVARCHAR(500)
                
        SELECT  @NoiDungDanhGia_SanPham_DanhSo = NoiDungDanhGia
        FROM    dbo.BPTC_BaoCaoTTSanPhamThang_DanhSo
        WHERE   BPTC_BaoCaoTTSanPhamThangREF = @ReportID
        
        SELECT  @NoiDungDanhGia_SanPham_ThucChay = NoiDungDanhGia
        FROM    dbo.BPTC_BaoCaoTTSanPhamThang_ThucChay
        WHERE   BPTC_BaoCaoTTSanPhamThangREF = @ReportID
        
        SELECT  @NoiDungDanhGia_SanPham_ThucChay_DanhSo = NoiDungDanhGia
        FROM    dbo.BPTC_BaoCaoTTSanPhamThang_ThucChay_DanhSo
        WHERE   BPTC_BaoCaoTTSanPhamThangREF = @ReportID
        
        SELECT  @PageFooter = N'# Dữ liệu cập nhật ngày '
                + CONVERT(NVARCHAR(10), NgayLap, 103) + ' (có VAT)' ,
                @PageHeader1 = N'Financial Department, '
                + CONVERT(NVARCHAR(10), NgayLap, 103) ,
                @NgayBatDau = ThoiGianBatDau ,
                @NgayKetThuc = ThoiGianKetThuc
        FROM    dbo.BPTC_BaoCaoTTSanPhamThang
        WHERE   BPTC_BaoCaoTTSanPhamThangID = @ReportID
        
        INSERT  INTO #COMMENT
                ( NoiDungDanhGia_SanPham_DanhSo ,
                  NoiDungDanhGia_SanPham_ThucChay ,
                  NoiDungDanhGia_SanPham_ThucChay_DanhSo ,
                  PageFooter ,
                  PageHeader1 ,
                  NgayBatDau ,
                  NgayKetThuc
                )
        VALUES  ( @NoiDungDanhGia_SanPham_DanhSo ,
                  @NoiDungDanhGia_SanPham_ThucChay ,
                  @NoiDungDanhGia_SanPham_ThucChay_DanhSo ,
                  @PageFooter ,
                  @PageHeader1 ,
                  @NgayBatDau ,
                  @NgayKetThuc
                )
        
        SELECT  *
        FROM    #COMMENT ;
        
        DROP TABLE #COMMENT
        
        --6. Lấy sản phẩm thuộc nhóm sản phẩm
        SELECT  TenSanPham
        FROM    dbo.DmNhomSanPhamBaoCao
        WHERE   DmNhomSanPhamBaoCaoID = @NhomSanPhamBaoCaoID
	
    END

```
